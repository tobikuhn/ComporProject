import random

from api.context_processors import get_current_week_number
from entities.WorkingHour import WorkingHour
from extensions import get_mysql_connection
from services.projects_service import get_projects_for_user
from services.user_service import get_all_users
from services.working_hours_service import put_working_hour, clear_working_hours


def mock_working_hours(user_id, calendar_week, mysql):
    wanted_weekly_hours = 4*45 +random.randrange(1,28)
    avg_hours_per_day = [40,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44]

    projects = get_projects_for_user(user_id, mysql=mysql)
    if len(projects) <= 0:
        print("No Projects found for User", user_id)
        return []
    working_hours = [WorkingHour(user_id, project.id, calendar_week, project.name) for project in projects]
    for day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
        hours_per_day = min(wanted_weekly_hours, random.choice(avg_hours_per_day))
        wanted_weekly_hours -= hours_per_day

        for _ in range(hours_per_day):
            chosen_project = random.choice(working_hours)
            setattr(chosen_project, day, getattr(chosen_project, day, 0) + 0.25)

    print(projects, working_hours)
    return working_hours


if __name__ == '__main__':
    clear_working_hours()
    mysql = get_mysql_connection()

    for user in get_all_users():
        print("Generating 8 weeks for User", user.id, user.name)
        current_calendar_week = get_current_week_number()
        current_calendar_week = current_calendar_week % 52
        for calendar_week in range(current_calendar_week - 8, current_calendar_week + 1):
            calendar_week = calendar_week % 52 
            print("-- Week", calendar_week)
            for working_hour in mock_working_hours(user.id, calendar_week, mysql=mysql):
                put_working_hour(working_hour, mysql=mysql)
