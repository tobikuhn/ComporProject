from entities.Project import Project
from extensions import get_mysql_connection


def get_projects_for_user(user_id):
    sql = """SELECT Project.id, Project.name
            FROM Project
                LEFT OUTER JOIN User_Project on Project.id = User_Project.project_id
            WHERE User_Project.user_id = """ + str(user_id)

    with get_mysql_connection().cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
        if result:
            return [Project(**r) for r in result]
        return []
