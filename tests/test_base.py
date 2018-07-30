import unittest

from app.views import app
from app.models import diaryEntries, users

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
        users[:] = []
