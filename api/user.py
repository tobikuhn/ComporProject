from flask import redirect
from flask.blueprints import Blueprint
from flask.globals import request
from flask.helpers import url_for
from flask.wrappers import Response
from flask_login.utils import login_user, logout_user
from werkzeug.exceptions import BadRequestKeyError

from extensions import login_manager
from services.user_service import get_user_by_id, verify_user_by_email

user_routes = Blueprint('user_routes', __name__, url_prefix="/")


@login_manager.user_loader
def load_user(user_id):
    return get_user_by_id(user_id)


@user_routes.route("/logout")
def logout():
    logout_user()

    return redirect(url_for("main_menu.main_menu"))


@user_routes.route("/login", methods=["POST"])
def login():
    try:
        username = request.form["username"]
        password = request.form["password"]
    except BadRequestKeyError:
        return Response(status=400)

    if username and password:
        user = verify_user_by_email(username, password)
        if user:
            if user.password == password:
                login_user(user, remember=True)

    return redirect(url_for("main_menu.main_menu"))
