class WorkingHour:
    def __init__(self, user_id, project_id, calendar_week, project_name, monday=0, tuesday=0, wednesday=0, thursday=0, friday=0):
        self.user_id = user_id
        self.project_id = project_id
        self.calendar_week = calendar_week
        self.project_name = project_name

        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
