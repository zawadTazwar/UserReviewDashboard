import unittest
from bottle import request, response
from bson import ObjectId
from webtest import TestApp
from server import app
from unittest.mock import MagicMock
from session_management import create_session, manage_sessions, delete_session, get_session, sessions


class TestServer(unittest.TestCase):
    def setUp(self):
        self.test_app = TestApp(app)
        self.sessions_collection = MagicMock()

    def test_home_page(self):
        response = self.test_app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.test_app.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        # Test a successful login
        response = self.test_app.post('/login', params={
            'username': 'jpwheeler',
            'password': 'jason1234'
        })
        self.assertIn(response.status_code, [302, 303])  # Check for a redirect (302 or 303)

        # Test an unsuccessful login with incorrect password
        response = self.test_app.post('/login', params={
            'username': 'jpwheeler',
            'password': 'incorrect_password'
        })
        self.assertEqual(response.status_code, 200)  # Should stay on the login page

    def test_profile_page(self):
        # Assuming you have a valid session
        response = self.test_app.get('/profile')
        self.assertIn(response.status_code, [200, 302, 303])  # Check for a valid response

    def test_signup_page(self):
        response = self.test_app.get('/signup')
        self.assertEqual(response.status_code, 200)

    def test_create_review_page(self):
        response = self.test_app.get('/create_review')
        self.assertEqual(response.status_code, 200)

    def test_reviews_page(self):
        response = self.test_app.get('/reviews')
        self.assertEqual(response.status_code, 200)

    def test_like_review(self):
        # You can simulate a 'like' or 'dislike' post request here
        response = self.test_app.post('/like_review/65492e9a717a81861104b2b4', params={
            'action': 'like'
        })
        self.assertIn(response.status_code, [302, 303])  # Check for a redirect

    def test_logout(self):
        response = self.test_app.get('/logout')
        self.assertIn(response.status_code, [302, 303])  # Check for a redirect after logging out

    def test_edit_review_page(self):
        # Simulate editing a review
        response = self.test_app.get('/edit_review/65492e9a717a81861104b2b4')
        self.assertEqual(response.status_code, 200)  # Check that the edit review page is accessible


    def test_create_session(self):
        # Assuming you have user data
        user_id = 1
        username = 'testuser'
        password = 'testpassword'
        first_name = 'Test'
        last_name = 'User'
        email = 'testuser@example.com'

        session_id = create_session(user_id, username, password, first_name, last_name, email,
                                    self.sessions_collection)
        # You might want to check if the session_id is not None or some other verification
        self.assertIsNotNone(session_id)

    def delete_session(session_id, sessions_collection):
        """
        Deletes the user session associated with the provided session ID.

        Args:
            session_id (str): The session ID of the session to be deleted.
            sessions_collection (pymongo.collection.Collection): The MongoDB collection for storing sessions.

        Returns:
            None
        """
        # Convert session_id to ObjectId before querying MongoDB
        sessions_collection.delete_one({"_id": ObjectId(session_id)})

        # Remove the session data from the dictionary
        if session_id in sessions:
            del sessions[session_id]

    def test_manage_sessions_valid_session(self):
        request = MagicMock()
        request.get_cookie.return_value = 'test_session_id'

        # Set the 'session' attribute correctly
        request.session = {'username': 'testuser'}

        manage_sessions(request)
        self.assertEqual(request.session, {'username': 'testuser'})

    def test_manage_sessions_invalid_session(self):
        request = MagicMock()
        request.get_cookie.return_value = 'invalid_session_id'
        manage_sessions(self.sessions_collection)
        self.assertNotIn('session', request)

    def test_get_session_valid_session(self):
        request = MagicMock()
        request.get_cookie.return_value = 'test_session_id'
        # Set up a sample session in the global sessions dictionary
        sessions['test_session_id'] = {'username': 'testuser'}
        session = get_session(request)
        self.assertEqual(session, {'username': 'testuser'})

    def test_get_session_invalid_session(self):
        request = MagicMock()
        request.get_cookie.return_value = 'invalid_session_id'
        session = get_session(request)
        self.assertEqual(session, {})


if __name__ == '__main__':
    unittest.main()

    # run by `python -m unittest test_server` in terminal
