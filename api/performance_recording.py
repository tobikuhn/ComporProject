from flask import redirect
from flask.blueprints import Blueprint
from flask.globals import request
from flask.helpers import url_for
from flask.templating import render_template
from flask_login.utils import login_required

from api.context_processors import generate_server_signature, format_date_day_month, \
    generate_week_period_caption, get_current_week_number, generate_array_of_weekdays_for_week
from entities.WorkingHour import WorkingHour
from extensions import config
from services.projects_service import get_projects_for_user
from services.user_service import get_user_by_id
from services.working_hours_service import get_working_hour_for_user, put_working_hour

expense_recording_routes = Blueprint('performance_recording', __name__, url_prefix="/compor+/user/<user_id>/")


@expense_recording_routes.route("/aufwands-erfassung/week/<calendar_week>", methods=["GET"])
@login_required
def performance_recording(user_id, calendar_week=get_current_week_number()):
    user = get_user_by_id(user_id)

    working_hours = get_working_hour_for_user(user.id, calendar_week) or []
    projects = get_projects_for_user(user.id)

    projects_with_hours = list(map(lambda wh: wh.project_id, working_hours))

    for project in projects:
        if project.id not in projects_with_hours:
            working_hours.append(WorkingHour(user.id, project.id, calendar_week, project.name))

    return render_template("performance_recording.html",
                           company=config.company_name,
                           application=config.app_name,
                           user=user,
                           projects=projects,
                           working_hours=working_hours,
                           calendar_week=calendar_week,
                           weekdays=generate_array_of_weekdays_for_week())


@expense_recording_routes.route("/aufwands-erfassung/week/<calendar_week>", methods=["POST"])
@login_required
def expense_recording_submit(user_id, calendar_week=get_current_week_number()):
    user = get_user_by_id(user_id)

    working_hours = dict(map(lambda v: (v.project_id, v), get_working_hour_for_user(user.id, calendar_week) or []))

    for key in request.form.keys():
        # Cleanup irrelevant form data
        if key.startswith("start") or key.startswith("end") or key.startswith("i_"):
            pass
        else:
            # project_id_weekday --> 1_ProjectAlpha
            (project_id, weekday) = key.split("_")
            project_id = int(project_id)

            # get hours worked
            time = request.form.get(key)

            # if project has no work hours, create an entry
            if project_id not in working_hours.keys():
                working_hours[project_id] = WorkingHour(user.id, project_id, calendar_week, "")

            # patch working hour directly into WorkHour's dict
            working_hours[project_id].__dict__[weekday] = time

    for working_hour in working_hours.values():
        put_working_hour(working_hour)

    return redirect(
        url_for("performance_recording.performance_recording", user_id=user.id, calendar_week=calendar_week))


@expense_recording_routes.context_processor
def faking_processor():
    return dict(generate_server_signature=generate_server_signature,
                generate_array_of_weekdays_for_week=generate_array_of_weekdays_for_week,
                format_date_day_month=format_date_day_month,
                generate_week_period_caption=generate_week_period_caption)
