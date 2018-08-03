import unittest

from app.instance import app
from db import  DatabaseConnection

connection = DatabaseConnection()


class BaseTestCase(unittest.TestCase):
    """"This is the base class for test class"""
    def setUp(self):
        self.test_client = app.test_client()
        self.user_register_data = {
            "name": "Kato",
            "email": "kato@gmail.com",
            "password": "123456"
        }
        self.user_login_data = {
            "email": "kato@gmail.com",
            "password": "123456"
        }
        self.diary_entry_data = {
            "diaryTitle": "wedding Dm",
            "date": "1/2/2017",
            "diaryEntryBody": "This some message for the entry in the diary",
            "user_id": "1"
        }

        self.modified_diary_entry_data = {
            "diaryTitle": "Modified",
            "date": "1/2/2018",
            "diaryEntryBody": "This entry has been modified"
        }
    def tearDown(self):
        cursor = connection.cursor
        # cursor.execute("""TRUNCATE TABLE users RESTART IDENTITY CASCADE""")
        cursor.execute(
            """TRUNCATE TABLE entries , users RESTART IDENTITY CASCADE""")


