from flask.blueprints import Blueprint
from flask.templating import render_template
from flask_login.utils import login_required, current_user

from api.context_processors import generate_date_from_month, generate_server_timestamp
from extensions import config
from services.projects_service import get_projects_for_user

reports_routes = Blueprint('reports', __name__)


@reports_routes.route("/compor+/berichte", methods=["GET"])
@login_required
def reports():
    return render_template("reports.html",
                           company=config.company_name,
                           application=config.app_name,
                           username=current_user.generate_username(),
                           projects=get_projects_for_user(current_user.id))


@reports_routes.route("/compor+/berichte/leistungsnachweis", methods=["GET"])
@login_required
def performance_record():
    return render_template("reports.performance_report.html",
                           company=config.company_name,
                           user_name=current_user.name,
                           project=get_projects_for_user(current_user.id))


@reports_routes.context_processor
def faking_processor():
    return dict(generate_date_from_month=generate_date_from_month, generate_server_timestamp=generate_server_timestamp)
