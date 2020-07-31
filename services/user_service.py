from entities.User import User
from extensions import get_mysql_connection


def get_user_by_id(user_id):
    with get_mysql_connection().cursor() as cursor:
        sql = "SELECT * FROM main.User WHERE id = " + str(user_id)
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            return User(**result)


def get_user_by_email(email):
    with get_mysql_connection().cursor() as cursor:
        sql = "SELECT * FROM main.User WHERE username = %s"
        cursor.execute(sql, email)
        result = cursor.fetchone()
        if result:
            return User(**result)
