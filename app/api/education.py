""" Ruta para los Datos Académicos de un Usuario """
from flask_restful import Resource
from flask_login import current_user
from app.model.db_config import db_session
from app.model.models import Education
from app.model.schema.schemas import education_schema

class EducationExperience(Resource):
    """ Recurso para los Datos Académicos de un Usuario """

    def get(self):
        """ Método de Obtención de todos los Datos Académicos de un Usuario """
        user_education = db_session.query(Education).filter(Education.user_email == current_user.email).all()

        return education_schema.dump(user_education, many=True)
