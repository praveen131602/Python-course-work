from library.models.admin import Admin

class Authservice:
    def __init__(self):
        self.admin = Admin("admin", "1234")

    def login(self, username, password):
        return username == self.admin.username and password == self.admin.password
