"""Archivo con los test de Autenticación de la Aplicación de Flask"""
from flask import current_app
from flask_testing import TestCase
from index import app
from app.model.db_config import db_session
from app.model.user import User
from app.utils.hash_password import hash_password

class AuthTest(TestCase):
    """Clase con los Test de Autenticación de la App"""

    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

        return app
    
    def test_register_user_response_when_success(self):
        """Test que verifica que la respuesta del Registro sea correcta"""
        user_test = {
            'email': 'pepe@pepe.com',
            'name': 'Pepe',
            'surname': 'Gonzalez',
            'address': 'San',
            'phone': '123456789',
            'password': '123456',
            'token': '123456789'
        }

        response = self.client.post('/register', data=user_test)
        self.assert200(response)
