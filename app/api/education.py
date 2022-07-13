""" Ruta para los Datos Académicos de un Usuario """
from flask import request
from flask_restful import Resource
from app.model.db_config import db_session
from app.model.models import Education, User
from app.model.schema.schemas import education_schema
from app.utils.decorators import token_required

class EducationExperience(Resource):
    """ Recurso para los Datos Académicos de un Usuario """

    @token_required
    def get(self):
        """ Método de Obtención de todos los Datos Académicos de un Usuario """

        token = request.headers['x-access-tokens']
        user_education = db_session.query(Education).filter(Education.user_email == User.email).filter(User.api_token == token).all()

        return education_schema.dump(user_education, many=True)
