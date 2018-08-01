import unittest

from app.instance import app
from db import  DatabaseConnection

connection = DatabaseConnection()


#Base test class for users
class BaseTestCaseUser(unittest.TestCase):
    """"This is the base class for user test class"""
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

    def tearDown(self):
        cursor = connection.cursor
        cursor.execute("""TRUNCATE TABLE users RESTART IDENTITY CASCADE""")




class BaseTestCaseDiaryEntry(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client()
        self.diary_entry_data = {
            "diaryTitle": "wedding Dm",
            "date": "1/2/2017",
            "diaryEntryBody": "This some message for the entry in the diary",
            "user_id":"1"
        }

    def tearDown(self):
        cursor = connection.cursor
        cursor.execute("""TRUNCATE TABLE entries RESTART IDENTITY CASCADE""")
