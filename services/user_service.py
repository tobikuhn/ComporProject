from entities.User import User


def get_user_by_id(mysql, user_id):
    with mysql.cursor() as cursor:
        sql = "SELECT * FROM main.User WHERE id = %s"
        cursor.execute(sql, user_id)
        result = cursor.fetchone()
        if result:
            return User(**result)


def get_user_by_email(mysql, email):
    with mysql.cursor() as cursor:
        sql = "SELECT * FROM main.User WHERE username = %s"
        cursor.execute(sql, email)
        result = cursor.fetchone()
        if result:
            return User(**result)
