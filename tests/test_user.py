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
        response = self.test_client.post('/api/v1/auth/signup',
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
        response = self.test_client.post('/api/v1/auth/signup', data=json.dumps(
            {"name": "", "email": "kato@gmail.com", "password": "12345"}),
            content_type='application/json')
        self.assertEqual(response.status_code, 400)

    #user login tests
    def test_user_login_without_all_data(self):
        """Function to check unsuccesful user login with empty fields"""
        response = self.test_client.post(
            '/api/v1/auth/login', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("All fields are required", str(response.data))

    def test_user_login_with_all_data(self):
        """Function to check successful user login"""
        response = self.test_client.post(
            '/api/v1/auth/login', data=json.dumps(self.user_login_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Welcome Kato. You are logged in", str(response.data))

    def test_login_without_password(self):
        """Function to check user login without password fails"""
        response = self.test_client.post('/api/v1/auth/login', data=json.dumps(
            {"email": "kato@gmail.com", "password": ""}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('password  is required', str(response.data))

    def test_login_without_email(self):
        """Function to check user login without email fails"""
        response = self.test_client.post('/api/v1/auth/login', data=json.dumps(
            {"email": "", "password": "123456"}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('email is required', str(response.data))
