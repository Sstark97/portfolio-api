"""Archivo que crea la Aplicación de Flask"""
from flask import Flask
from flask_login import LoginManager

def create_app():
    """Crea la Aplicación de Flask"""
    app = Flask(__name__, static_folder='static', template_folder='view')
    app.env = 'development'

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from app.model.user import User

    @login_manager.user_loader
    def load_user(user_email):
        """Carga el usuario"""
        return User.query.get(user_email)

    return app
