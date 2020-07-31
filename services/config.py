from services.mysql_config import MySQLConfig


class FlaskConfig:
    # SHA-256 "Compor AG 2020"
    SECRET_KEY = "207d1dd413d28b46940340499013aa24f66d2e5d5002726572c5396428cc71fe"
    # mysql://root:toor@192.168.129.142:3306/main


class AppConfig(FlaskConfig, MySQLConfig):
    company_name = "Compor AG"
    app_name = "Compor+"
    company_email = "compor_plus@compor-ag.de"
