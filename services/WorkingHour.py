class WorkingHour:
    def __init__(self, user_id, project_id, calendar_week, project_name, monday=0, tuesday=0, wednesday=0, thursday=0,
                 friday=0):
        self.user_id = user_id
        self.project_id = project_id
        self.calendar_week = calendar_week
        self.project_name = project_name

        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday

    def set_days(self, monday=0, tuesday=0, wednesday=0, thursday=0, friday=0):
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday

    def __repr__(self):
        return "User.id: {}, Project.id: {}, Project.name: {}, Calendar Week: {}: Mo: {}, Tu: {}, We: {}, Th: {}, Fr: {}" \
            .format(self.user_id, self.project_id, self.project_name, self.calendar_week, self.monday, self.tuesday,
                    self.wednesday, self.thursday, self.friday)
