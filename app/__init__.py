"""Archivo que crea la Aplicación de Flask"""
from flask import Flask
from flask_login import LoginManager
from app.controller.controllers import auth, account, projects, work
from app.model.db_config import init_db

def create_app():
    """Crea la Aplicación de Flask"""
    app = Flask(__name__, static_folder='static', template_folder='view')
    app.env = 'development'

    app.register_blueprint(auth)
    app.register_blueprint(account)
    app.register_blueprint(projects)
    app.register_blueprint(work)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    init_db()

    from app.model.user import User

    @login_manager.user_loader
    def load_user(user_email):
        """Carga el usuario"""
        return User.query.get(user_email)

    return app
