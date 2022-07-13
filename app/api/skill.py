""" Ruta para las Habilidades de un Usuario """
from flask import request
from flask_restful import Resource
from app.model.db_config import db_session
from app.model.models import Skill, User
from app.model.schema.schemas import skills_schema
from app.utils.decorators import token_required

class Skills(Resource):
    """ Recurso para obtener las Habilidades de un Usuario """

    @token_required
    def get(self):
        """ Método de Obtención de las Habilidades de un Usuario """

        token = request.headers['x-access-tokens']
        user_skills = db_session.query(Skill).filter(Skill.user_email == User.email).filter(User.api_token == token).all()

        return skills_schema.dump(user_skills, many=True)
