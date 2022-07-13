""" Ruta para los datos de un Usuario """
from flask import request
from flask_restful import Resource
from app.model.db_config import db_session
from app.model.models import User
from app.model.schema.schemas import user_schema
from app.utils.decorators import token_required

class UserAllData(Resource):
    """ Recurso para manejar todos los datos de un Usuario """

    @token_required
    def get(self):
        """ Método de Obtención de los datos de un Usuario """

        token = request.headers['x-access-tokens']
        user_data = db_session.query(User).filter(User.api_token == token).first()

        return user_schema.dump(user_data)


class UserData(Resource):
    """ Recurso para manejar los datos de un Usuario """

    @token_required
    def get(self):
        """ Método de Obtención de los datos de un Usuario """

        token = request.headers['x-access-tokens']
        user_data = db_session.query(User.email, User.name, User.surname, User.presentation,
                                     User.adress, User.phone, User.avatar).filter(User.api_token == token).first()

        return user_schema.dump(user_data)
