class User:

    def __init__(self, id, username, password, name, role):
        self.id = id
        self.username = username
        self.password = password
        self.name = name
        self.role = role

    def generate_username(self):
        split = self.name.split(" ")
        return split[0][:1].lower() + split[1].lower()

    @staticmethod
    def is_authenticated(self):
        return True

    @staticmethod
    def is_active(self):
        return True

    @staticmethod
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
