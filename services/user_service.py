from entities.User import User
from extensions import get_mysql_connection


def change_user_password(user_id, new_password):
    sql = "UPDATE User SET password = '" + new_password + "' WHERE id = " + str(user_id)
    with get_mysql_connection().cursor() as cursor:
        cursor.execute(sql)
        return True


def get_user_by_id(user_id):
    with get_mysql_connection().cursor() as cursor:
        sql = "SELECT * FROM User WHERE id = " + str(user_id)
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            return User(**result)


def get_user_by_email(email):
    with get_mysql_connection().cursor() as cursor:
        sql = "SELECT * FROM User WHERE email = %s"
        cursor.execute(sql, email)
        result = cursor.fetchone()
        if result:
            return User(**result)


def verify_user_by_email(email, password):
    with get_mysql_connection().cursor() as cursor:
        sql = "SELECT * FROM User WHERE email = %s AND password = '" + password + "'"
        cursor.execute(sql, email)
        result = cursor.fetchone()
        if result:
            return User(**result)


def get_user_count():
    with get_mysql_connection().cursor() as cursor:
        sql = "SELECT COUNT(*) FROM User"
        cursor.execute(sql)
        result = cursor.fetchone()

        if result:
            return result["COUNT(*)"]
