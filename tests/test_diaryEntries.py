import  json
from app.instance import app
from .test_base import BaseTestCaseDiaryEntry



class EntriesTest(BaseTestCaseDiaryEntry):
        #tests for creating diary entry
    def test_create_entry(self):
        """ Tests whether a user can create an entry successfully """
        response = self.test_client.post(
            '/api/v1/auth/signup', data=json.dumps(self.user_register_data),
            content_type='application/json')
        response = self.test_client.post(
            '/api/v1/entries', data=json.dumps(self.diary_entry_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("You have successfully created your entry",
                      str(response.data))

    def test_create_entry_without_data(self):
        """ Tests whether a user can create an entry without data """
        response = self.test_client.post(
            '/api/v1/entries', data=json.dumps({}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("Enter data in all fields", str(response.data))

    def test_create_entry_without_title(self):
        """ Tests whether a user can not create an entry without a title """
        response = self.test_client.post('/api/v1/entries', data=json.dumps(
            {"diaryTitle": "", "date": "2/2/2017", "diaryBody": "Entry without title"}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Title is required', str(response.data))

    def test_create_entry_without_date(self):
        """ Tests whether a user can not create an entry without a date """
        response = self.test_client.post('/api/v1/entries', data=json.dumps(
            {"diaryTitle": "Wed", "date": "", "diaryBody": "Entry without title"}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('date is required', str(response.data))

    def test_create_entry_without_body(self):
        """ Tests whether a user can not create an entry without a body """
        response = self.test_client.post('/api/v1/entries', data=json.dumps(
            {"diaryTitle": "Wed", "date": "2/5/2018", "diaryBody": ""}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Field required: Please write someting',
                      str(response.data))

    #tests for fetching all entries
    def test_get_all_entries_empty(self):
        """ Tests whether a user can't fetch entries when none exists """
        response = self.test_client.get(
            '/api/v1/entries', content_type='application/json')
        self.assertEqual(response.status_code, 404)
        self.assertIn('You have no entries', str(response.data))

    def test_get_all_entries(self):
        """ Tests whether a user can get all entries """
        response = self.test_client.post(
            '/api/v1/entries', data=json.dumps(self.diary_entry_data), content_type='application/json')
        response = self.test_client.get(
            '/api/v1/entries', content_type='application/json')
        self.assertEqual(response.status_code, 200)
