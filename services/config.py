from services.mysql_config import MySQLConfig


class FlaskConfig:
    # SHA-256 "Compor AG 2020"
    SECRET_KEY = "207d1dd413d28b46940340499013aa24f66d2e5d5002726572c5396428cc71fe"
    APPLICATION_ROOT = "/compor+"


class AppConfig(FlaskConfig, MySQLConfig):
    company_name = "Compor AG"
    app_name = "Compor Project"
    company_email = "compor_project@compor-ag.de"
