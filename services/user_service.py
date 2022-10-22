from entities.User import User
from extensions import get_mysql_connection
from .debug_sql import debug_sql

def change_user_password(user_id, new_password):
    sql = "UPDATE User SET password = '" + new_password + "' WHERE id = " + str(user_id)
    debug_sql(sql)
    with get_mysql_connection().cursor() as cursor:
        cursor.execute(sql)
        return True


def get_user_by_id(user_id):
    with get_mysql_connection().cursor() as cursor:
        sql = "SELECT * FROM User WHERE id = " + str(user_id)
        debug_sql(sql)
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            return User(**result)


def get_user_by_email(email):
    with get_mysql_connection().cursor() as cursor:
        sql = "SELECT * FROM User WHERE email = '" +email + "'"
        debug_sql(sql)
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            return User(**result)


def verify_user_by_email(email, password):
    with get_mysql_connection().cursor() as cursor:
        sql = "SELECT * FROM User WHERE email = '" +email + "' AND password = '" + password + "'"
        debug_sql(sql)
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            return User(**result)


def get_user_count():
    with get_mysql_connection().cursor() as cursor:
        sql = "SELECT COUNT(*) FROM User"
        debug_sql(sql)
        cursor.execute(sql)
        result = cursor.fetchone()

        if result:
            return result["COUNT(*)"]


def get_all_users():
    with get_mysql_connection().cursor() as cursor:
        sql = "SELECT * FROM User"
        debug_sql(sql)
        cursor.execute(sql)
        result = cursor.fetchall()

        if result:
            return [User(**r) for r in result] if result else []
