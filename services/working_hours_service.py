from api.context_processors import get_current_week_number
from entities.WorkingHour import WorkingHour
from extensions import get_mysql_connection


def get_working_hour_for_user(user_id, calendar_week=get_current_week_number()):
    sql = """  SELECT WorkingHour.user_id,
                      Project.id AS project_id,
                      Project.name as project_name,
                      WorkingHour.calendar_week,
                      WorkingHour.monday,
                      WorkingHour.tuesday,
                      WorkingHour.wednesday,
                      WorkingHour.thursday,
                      WorkingHour.friday
               FROM WorkingHour, Project
               WHERE WorkingHour.project_id = Project.id
                 AND WorkingHour.user_id = """ + str(user_id) + """
                 AND WorkingHour.calendar_week = """ + str(calendar_week)

    with get_mysql_connection().cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
        if result:
            return [WorkingHour(**r) for r in result] or []


def put_working_hour(working_hours, mysql=None):
    values = [working_hours.user_id, working_hours.project_id, working_hours.calendar_week,
              working_hours.monday, working_hours.tuesday, working_hours.wednesday,
              working_hours.thursday, working_hours.friday]

    values_sql = "'" + "', '".join(map(lambda x: str(x), values)) + "'"

    sql = """ REPLACE INTO WorkingHour (user_id, project_id, calendar_week, monday, tuesday, wednesday, thursday, friday)
              VALUES(""" + values_sql + ")"

    with (mysql or get_mysql_connection()).cursor() as cursor:
        cursor.execute(sql)


def get_project_hours_per_day(user_id, calendar_week, day):
    sql = """   SELECT Project.name, WorkingHour.""" + day + """
                FROM  WorkingHour
                    INNER JOIN Project on WorkingHour.project_id = Project.id
                WHERE WorkingHour.calendar_week = """ + str(calendar_week) + """
                AND WorkingHour.user_id = """ + str(user_id)

    with get_mysql_connection().cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()

        return result if result else []


def get_available_calendar_weeks(user_id):
    sql = "SELECT DISTINCT WorkingHour.calendar_week FROM WorkingHour WHERE WorkingHour.user_id = " + str(user_id)

    with get_mysql_connection().cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
        if result:
            return result

        return []


def clear_working_hours():
    with get_mysql_connection().cursor() as cursor:
        cursor.execute("TRUNCATE TABLE WorkingHour")
