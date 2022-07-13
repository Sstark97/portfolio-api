""" Ruta para los Hobbies de un Usuario """
from flask import request
from flask_restful import Resource
from app.model.db_config import db_session
from app.model.models import Hobby, User
from app.model.schema.schemas import hobbies_schema
from app.utils.decorators import token_required

class Hobbies(Resource):
    """ Recurso para obtener los Hobbies de un Usuario """

    @token_required
    def get(self):
        """ Método de Obtención de los Hobbies de un Usuario """
        
        token = request.headers['x-access-tokens']
        user_hobbies = db_session.query(Hobby).filter(Hobby.user_email == User.email).filter(User.api_token == token).all()

        return hobbies_schema.dump(user_hobbies, many=True)
