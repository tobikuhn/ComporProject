from flask import Flask


def create_app() -> Flask:
    flask_app = Flask(__name__)

    from services.config import FlaskConfig
    flask_app.config.from_object(FlaskConfig)

    register_blueprints(flask_app)
    register_extensions(flask_app)

    return flask_app


def register_blueprints(flask_app: Flask):
    from api.main_menu import main_menu_routes
    flask_app.register_blueprint(main_menu_routes)

    from api.performance_recording import expense_recording_routes
    flask_app.register_blueprint(expense_recording_routes)

    from api.reports import reports_routes
    flask_app.register_blueprint(reports_routes)

    from api.user import user_routes
    flask_app.register_blueprint(user_routes)


def register_extensions(flask_app):
    from extensions import login_manager
    login_manager.init_app(flask_app)


app = create_app()
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
