"""Archivo que crea la Aplicación de Flask"""
from flask import Flask
from flask_restful import Api
from flask_login import LoginManager
from app.controller.controllers import auth, account, projects, work, education, hobby, skill, docs
from app.api.resources import Hobbies, Skills, WorkExperience, EducationExperience, Projects, UserAllData, UserData
from app.model.db_config import init_db
from app.model.schema.schema_config import ma

def create_app():
    """Crea la Aplicación de Flask"""
    app = Flask(__name__, static_folder='static', template_folder='view')
    app.env = 'development'

    app.register_blueprint(auth)
    app.register_blueprint(account)
    app.register_blueprint(projects)
    app.register_blueprint(work)
    app.register_blueprint(education)
    app.register_blueprint(hobby)
    app.register_blueprint(skill)
    app.register_blueprint(docs)

    api = Api(app, catch_all_404s=True)
    api.add_resource(Hobbies, '/api/v1/hobbies')
    api.add_resource(Skills, '/api/v1/skills')
    api.add_resource(WorkExperience, '/api/v1/work')
    api.add_resource(EducationExperience, '/api/v1/education')
    api.add_resource(Projects, '/api/v1/projects')
    api.add_resource(UserData, '/api/v1/user')
    api.add_resource(UserAllData, '/api/v1/user/all')

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    init_db()
    ma.init_app(app)

    from app.model.user import User

    @login_manager.user_loader
    def load_user(user_email):
        """Carga el usuario"""
        return User.query.get(user_email)

    return app
