
users = []
class UsersModel:
    """This class is used to create user instances"""

    def __init__(self, name, email,password):
        self.name = name
        self.email = email
        self.password = password
    
    def insert_user(self):
        users.append(self)

