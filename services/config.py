class FlaskConfig:
    # SHA-256 "Compor AG 2020"
    SECRET_KEY = "207d1dd413d28b46940340499013aa24f66d2e5d5002726572c5396428cc71fe"

    MYSQL_DATABASE_HOST = "192.168.129.142"
    MYSQL_DATABASE_PORT = 3036
    MYSQL_DATABASE_USER = "root"
    MYSQL_DATABASE_PASSWORD = "toor"
    MYSQL_DATABASE_DB = "main"


class AppConfig(FlaskConfig):
    company_name = "Compor AG"
    app_name = "Compor+"
    company_email = "compor_plus@compor-ag.de"
