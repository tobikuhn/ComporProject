from flask import redirect
from flask.blueprints import Blueprint
from flask.globals import request
from flask.helpers import url_for
from flask.templating import render_template
from flask.wrappers import Response
from flask_login.utils import login_user, logout_user, login_required, current_user
from werkzeug.exceptions import BadRequestKeyError

from api.context_processors import generate_server_signature
from extensions import login_manager, config
from services.user_service import get_user_by_id, verify_user_by_email, change_user_password

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


@user_routes.route("/user-editor", methods=["GET", "POST"])
@login_required
def user_editor():
    msg = None
    if request.method == "POST":
        try:
            password = request.form["password"]
        except BadRequestKeyError:
            return Response(status=400)

        change_user_password(current_user.id, password)
        msg = "Password changed"


    return render_template("user_editor.html",
                           company=config.company_name,
                           application=config.app_name,
                           user=current_user,
                           msg=msg)


@user_routes.context_processor
def faking_processor():
    return dict(generate_server_signature=generate_server_signature)
