from flask_login.mixins import UserMixin


class User(UserMixin):

    def __init__(self, id, email, password, name):
        self.id = id
        self.email = email
        self.password = password
        self.name = name

    def generate_username(self):
        split = self.email.split("@")
        return split[0]
