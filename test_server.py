import unittest
from bottle import request, response
from webtest import TestApp
from server import app


class TestServer(unittest.TestCase):
    def setUp(self):
        self.test_app = TestApp(app)

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

    def test_update_review(self):
        # Simulate updating a review
        response = self.test_app.post('/update_review', params={
            'review_id': '65492e9a717a81861104b2b4',
            'content': 'Updated review content.'
        })
        self.assertIn(response.status_code, [302, 303])  # Check for a redirect after updating the review


if __name__ == '__main__':
    unittest.main()

    # run by `python -m unittest test_server` in terminal
