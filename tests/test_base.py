"""Archivo con los test base de la Aplicación de Flask"""
from flask import current_app
from flask_testing import TestCase
from index import app

class MainTest(TestCase):

    """Clase con los Test principales de la App"""

    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        return app

    def test_app_exists(self):
        """Test que verifica que la Aplicación exista"""
        self.assertIsNotNone(app)
        
    def test_app_in_test_mode(self):
        """Test que verifica que la Aplicación esté en modo Test"""
        self.assertTrue(current_app.config['TESTING'])
