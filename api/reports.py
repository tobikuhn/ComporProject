from flask import redirect
from flask.blueprints import Blueprint
from flask.globals import request
from flask.helpers import send_file, url_for
from flask.templating import render_template
from flask_login.utils import login_required, current_user

from api.context_processors import generate_month_year_display, generate_server_signature, get_current_date, \
    get_current_week_number
from extensions import config
from services.projects_service import get_projects_for_user
from services.report_service import save_report, resolve_report_file
from services.user_service import get_user_by_id
from services.working_hours_service import get_project_hours_per_day, get_available_calendar_weeks

reports_routes = Blueprint('reports', __name__, url_prefix="/user/<user_id>/")


@reports_routes.route("/berichte", methods=["GET"])
@login_required
def reports(user_id):
    user = get_user_by_id(user_id)
    calendar_weeks = get_available_calendar_weeks(user_id)
    return render_template("reports.html",
                           company=config.company_name,
                           application=config.app_name,
                           user=current_user,
                           projects=get_projects_for_user(user.id),
                           calendar_weeks=calendar_weeks,
                           calendar_week=get_current_week_number())


@reports_routes.route("/berichte/leistungsnachweis/week/<calendar_week>",
                      methods=["GET", "POST"])
@login_required
def performance_record(user_id, calendar_week):
    user = get_user_by_id(user_id)

    work_per_days = []

    for day in [("monday", "Montag"), ("tuesday", "Dienstag"),
                ("wednesday", "Mittwoch"), ("thursday", "Donnerstag"), ("friday", "Freitag")]:

        for w in get_project_hours_per_day(user_id, calendar_week, day[0]):
            work_per_days.append({"day": day[1], "project": w["name"], "work": w[day[0]]})

    sum_work = 0
    for w in work_per_days:
        try:
            sum_work += int(w["work"])
        except ValueError:
            # for invalid time strings
            pass

    rendered_html = render_template("reports.performance_report.html",
                                    company=config.company_name,
                                    user_name=user.name,
                                    calendar_week=calendar_week,
                                    sum_work=sum_work,
                                    work=work_per_days)
    report_filename = save_report(rendered_html)
    return redirect(url_for("reports.report_file", user_id=current_user.id, file=report_filename))


@reports_routes.route("/berichte/leistungsnachweis/")
@login_required
def report_file(user_id):
    return send_file(resolve_report_file(request.values.get("file")))


@reports_routes.context_processor
def faking_processor():
    return dict(generate_date_from_month=generate_month_year_display,
                generate_server_signature=generate_server_signature,
                get_current_date=get_current_date)
