""" Ruta para los Proyectos de un Usuario """
from flask_restful import Resource
from flask_login import current_user
from app.model.db_config import db_session
from app.model.models import Project
from app.model.schema.project_schema import project_schema

class Projects(Resource):
    """ Recurso para los Proyectos de un Usuario """

    def get(self):
        """ Método de Obtención de todos los Proyectos de un Usuario """
        user_projects = db_session.query(Project).filter(Project.user_email == current_user.email).all()

        return project_schema.dump(user_projects, many=True)
