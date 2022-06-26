from flask import current_app, url_for
from flask_testing import TestCase
from index import app

class MainTest(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        return app
    
    def test_app_exists(self):
        self.assertIsNotNone(app)
    
    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])