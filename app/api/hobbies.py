""" Ruta para los Hobbies de un Usuario """
from flask_restful import Resource
from flask_login import current_user
from app.model.db_config import db_session
from app.model.models import Hobby
from app.model.schema.hobbies_schema import hobbies_schema

class Hobbies(Resource):
    """ Recurso para obtener los Hobbies de un Usuario """

    def get(self):
        """ Método de Obtención de los Hobbies de un Usuario """
        user_hobbies = db_session.query(Hobby).filter(Hobby.user_email == current_user.email).all()

        return hobbies_schema.dump(user_hobbies, many=True)
