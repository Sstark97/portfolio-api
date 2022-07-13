""" Ruta para la Experiencia laboral de un Usuario """
from flask import request
from flask_restful import Resource
from app.model.db_config import db_session
from app.model.models import Work, User
from app.model.schema.schemas import work_schema
from app.utils.decorators import token_required

class WorkExperience(Resource):
    """ Recurso para la Experiencia laboral de un Usuario """

    @token_required
    def get(self):
        """ Método de Obtención de toda la Experiencia laboral de un Usuario """

        token = request.headers['x-access-tokens']
        user_work = db_session.query(Work).filter(Work.user_email == User.email).filter(User.api_token == token).all()

        return work_schema.dump(user_work, many=True)
