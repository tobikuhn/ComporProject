
from datetime import datetime, timedelta

from extensions import config


def generate_date_from_now(offset, hour):
    date = datetime.now().replace(hour=hour) + timedelta(days=offset)
    # 23.07.2020 12:00
    return date.strftime("<b>%d.%m.%Y %H:00</b>")


def get_current_date():
    return datetime.now().strftime("%d.%m.%Y")


def get_current_year():
    return datetime.now().strftime("%Y")


def generate_server_signature():
    date = datetime.now()
    return date.strftime("%H:%M:%S %d.%m.%Y") + " © " + config.company_name + " " + date.strftime("%Y") + " v13785"


def generate_month_year_display(month=None):
    date = datetime.now()
    if month:
        # Day has to be below 28, in case the month has only 28 days
        date = date.replace(month=month, day=1)

    return date.strftime("%m/%Y")


def get_current_week_number():
    return datetime.now().isocalendar()[1]


def get_monday_from_week_number(week_number):
    # https://stackoverflow.com/a/17087427
    week_number_ger = int(week_number) - int(1)
    d = get_current_year() + "-W" + str(week_number_ger)
    return datetime.strptime(d + '-1', "%Y-W%W-%w")


def generate_array_of_weekdays_for_week(week_number=get_current_week_number()):
    monday = get_monday_from_week_number(week_number)
    days = [monday]
    for day_idx in range(1, 5):
        days.append(monday + timedelta(days=day_idx))

    return days


def generate_week_period_caption(week_number=get_current_week_number()):
    monday = get_monday_from_week_number(week_number)
    friday = monday + timedelta(days=4)

    return monday.strftime("%d.%m.%y") + " bis " + friday.strftime("%d.%m.%y")


def format_date_day_month(date):
    return date.strftime("%d.%m.")
