from flask import redirect
from flask.blueprints import Blueprint
from flask.globals import request
from flask.helpers import url_for
from flask_login.utils import login_user, logout_user

from extensions import login_manager, mysql
from services.user_service import get_user_by_id, get_user_by_email

user_routes = Blueprint('user_routes', __name__)


@login_manager.user_loader
def load_user(user_id):
    return get_user_by_id(mysql, user_id)


@user_routes.route("/compor+/logout")
def logout():
    logout_user()

    return redirect(url_for("main_menu.main_menu"))


@user_routes.route("/compor+/login", methods=["GET", "POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username and password:
        user = get_user_by_email(mysql, request.form["username"])
        if user:
            if user.password == password:
                login_user(user)

    return redirect(url_for("main_menu.main_menu"))
