from flask import redirect
from flask.blueprints import Blueprint
from flask.globals import request
from flask.helpers import url_for
from flask.templating import render_template
from flask_login.utils import current_user, login_required

from api.context_processors import generate_server_timestamp, generate_array_of_current_weekdays, format_date_day_month, \
    generate_week_period_caption
from extensions import config
from services.projects_service import get_projects_for_user

expense_recording_routes = Blueprint('expense_recording', __name__)


@expense_recording_routes.route("/compor+/aufwands-erfassung", methods=["GET"])
@login_required
def expense_recording():
    return render_template("performance_recording.html",
                           company=config.company_name,
                           application=config.app_name,
                           username=current_user.username,
                           projects=get_projects_for_user(current_user.id))


@expense_recording_routes.route("/compor+/aufwands-erfassung/data", methods=["POST"])
@login_required
def expense_recording_data():
    print(request.form)
    return redirect(url_for("expense_recording.expense_recording"))


@expense_recording_routes.context_processor
def faking_processor():
    return dict(generate_server_timestamp=generate_server_timestamp,
                generate_array_of_current_weekdays=generate_array_of_current_weekdays,
                format_date_day_month=format_date_day_month,
                generate_week_period_caption=generate_week_period_caption)
