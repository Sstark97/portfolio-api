""" Ruta para los Proyectos de un Usuario """
from flask_restful import Resource
from flask import request
from app.model.db_config import db_session
from app.model.models import Project, User
from app.model.schema.schemas import project_schema
from app.utils.decorators import token_required

class Projects(Resource):
    """ Recurso para los Proyectos de un Usuario """

    @token_required
    def get(self):
        """ Método de Obtención de todos los Proyectos de un Usuario """
        token = request.headers['x-access-tokens']
        user_projects = db_session.query(Project).filter(Project.user_email == User.email).filter(User.api_token == token).all()

        return project_schema.dump(user_projects, many=True)
