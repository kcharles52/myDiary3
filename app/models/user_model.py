from db import DatabaseConnection
conn = DatabaseConnection()


class UsersModel():
    """This class is used to create user instances"""

    def __init__(self, name, email,password):
        self.name = name
        self.email = email
        self.password = password

    def insert_user(self):
        conn.cursor.execute("""INSERT INTO users(name,email,password) VALUES (%s,%s,%s) """, (self.name, self.email, self.password))

    @staticmethod
    def fetch_user(email):
        conn.cursor.execute("""SELECT * FROM users WHERE email=%s""",[email])
        fetch_user = conn.cursor.fetchone()
        fetched_user = fetch_user
        return fetched_user