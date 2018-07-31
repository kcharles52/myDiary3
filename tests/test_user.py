import json
from .test_base import BaseTestCaseUser
from app.instance import app

class UserTest(BaseTestCaseUser):

    #User registration tests
    def test_register_user_without_data(self):
        """Function to test if a user can register without providing data"""
        response = self.test_client.post(
            '/api/v1/auth/signup', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('All fields are required', str(response.data))


    def test_register_user(self):
        """Function to test if a user can register successfully"""
        response = self.test_client.post(
            '/api/v1/auth/signup', data=json.dumps(self.user_register_data),
            content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('User Kato has been registered', str(response.data))

    def test_register_user_without_email(self):
        """Function to test user registration without email fails"""
        response = self.test_client.post('/api/v1/auth/sigup',
         data=json.dumps({"name":"kato","email":"","password":"12345"}),
         content_type='application/json')
        self.assertEqual(response.status_code,400)

    def test_register_user_without_password(self):
        """Function to test user registration without password fails"""
        response = self.test_client.post('/api/v1/auth/signup', data=json.dumps(
            {"name": "kato", "email": "kato@gmail.com", "password": ""}),
            content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_register_user_without_name(self):
        """Function to test user registration without name fails"""
        response = self.test_client.post('/api/v1/users', data=json.dumps(
            {"name": "", "email": "kato@gmail.com", "password": "12345"}),
            content_type='application/json')
        self.assertEqual(response.status_code, 400)


