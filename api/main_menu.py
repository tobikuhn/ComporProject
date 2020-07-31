from flask.blueprints import Blueprint
from flask.templating import render_template
from flask_login.utils import current_user

from api.context_processors import generate_date_from_now, generate_month_year_display, generate_server_signature, \
    get_current_week_number
from extensions import config

main_menu_routes = Blueprint('main_menu', __name__)


@main_menu_routes.route("/compor+", methods=["GET"])
def main_menu():
    return render_template("main_menu.html",
                           company=config.company_name,
                           application=config.app_name,
                           email=config.company_email,
                           user=current_user,
                           calendar_week=get_current_week_number())


@main_menu_routes.context_processor
def faking_processor():
    return dict(generate_date_from_now=generate_date_from_now,
                generate_date_from_month=generate_month_year_display,
                generate_server_signature=generate_server_signature)
