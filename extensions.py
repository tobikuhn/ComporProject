import pymysql
from flask_login.login_manager import LoginManager

from services.config import AppConfig

config = AppConfig

login_manager = LoginManager()

con = pymysql.connect(host=config.MYSQL_DATABASE_HOST,
                      user=config.MYSQL_DATABASE_USER,
                      password=config.MYSQL_DATABASE_PASSWORD,
                      db=config.MYSQL_DATABASE_DB,
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor,
                      autocommit=True)


def get_mysql_connection():
    return con
