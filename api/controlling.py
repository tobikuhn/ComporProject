from flask import redirect
from flask.blueprints import Blueprint
from flask.globals import request
from flask.helpers import send_file, url_for
from flask.templating import render_template
from flask_login.utils import login_required, current_user

from api.context_processors import generate_month_year_display, generate_server_signature, get_current_date, \
    get_current_week_number
from extensions import config
from services.projects_service import get_projects_for_user, get_all_projects
from services.report_service import save_report, resolve_report_file
from services.user_service import get_user_by_id, get_all_users, is_user_admin
from services.working_hours_service import get_project_hours_per_day, get_available_calendar_weeks, get_working_hour_for_user_in_project

controlling_routes = Blueprint('controlling', __name__, url_prefix="/")


@controlling_routes.route("/controlling", methods=["GET"])
@login_required
def controlling():
    calendar_week = request.values.get("calendar_week")
    if calendar_week:
        return performance_record(calendar_week)
    else:
        calendar_week = get_current_week_number()
        return performance_record(calendar_week)



def performance_record( calendar_week):
    #user = get_user_by_id(user_id)

    
    projects=get_all_projects()
    users=get_all_users() 
    calendar_weeks = get_available_calendar_weeks(1)
    last_project=""
    table = []
    for p in projects:
      for u in users:
          report = get_working_hour_for_user_in_project(u.id ,p.id,calendar_week)
          try:
              try:
                total = float(report[0].monday)+float(report[0].tuesday)+float(report[0].wednesday)+float(report[0].thursday)+float(report[0].friday)
              except:
                total = 0
              if last_project == p.id:
                table.append({"project": "", "user": get_user_by_id(u.id).name, "hours": [report[0].monday, report[0].tuesday, report[0].wednesday, report[0].thursday, report[0].friday], "total":total})  
              else:
                table.append({"project": p.name, "user": get_user_by_id(u.id).name, "hours": [report[0].monday, report[0].tuesday, report[0].wednesday, report[0].thursday, report[0].friday], "total":total})  
              last_project=p.id

          except:
            pass
    rendered_html = render_template("controlling.html",
                                    company=config.company_name,
                                    application=config.app_name,
                                    user_name=current_user.name,
                                    user=current_user,
                                    calendar_week=calendar_week,
                                    calendar_weeks=calendar_weeks,
                                    table=table,
                                    admin=is_user_admin(current_user.id)
                                    )
    return rendered_html

@controlling_routes.context_processor
def faking_processor():
    return dict(generate_date_from_month=generate_month_year_display,
                generate_server_signature=generate_server_signature,
                get_current_date=get_current_date)

