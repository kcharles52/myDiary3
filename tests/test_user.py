import json
from test_base import BaseTestCaseUser
from app.views import app

class UserTest(BaseTestCaseUser):

    #User registration tests
    def test_register_user_without_data(self):
        """Function to test if a user can register without providing data"""
        response = self.test_client.post(
            '/api/v1/auth/users', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('All fields are required', str(response.data))

