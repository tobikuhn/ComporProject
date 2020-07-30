from entities.Project import Project
from extensions import mysql


def get_projects_for_user(user_id):
    sql = """SELECT Project.id, Project.name
            FROM Project
                LEFT OUTER JOIN User_Project on Project.id = User_Project.project_id
            WHERE User_Project.user_id = %s
        """

    with mysql.cursor() as cursor:
        cursor.execute(sql, user_id)
        result = cursor.fetchall()
        if result:
            return [Project(**r) for r in result]
