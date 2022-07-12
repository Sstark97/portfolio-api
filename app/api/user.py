""" Ruta para los datos de un Usuario """
from flask_restful import Resource
from flask_login import current_user
from app.model.db_config import db_session
from app.model.models import User
from app.model.schema.schemas import user_schema

class UserData(Resource):
    """ Recurso para los datos de un Usuario """

    def get(self):
        """ Método de Obtención de los datos de un Usuario """
        user_data = db_session.query(User).filter(User.email == current_user.email).first()

        return user_schema.dump(user_data)
