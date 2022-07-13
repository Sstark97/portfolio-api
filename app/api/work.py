""" Ruta para la Experiencia laboral de un Usuario """
from flask_restful import Resource
from flask_login import current_user
from app.model.db_config import db_session
from app.model.models import Work
from app.model.schema.schemas import work_schema

class WorkExperience(Resource):
    """ Recurso para la Experiencia laboral de un Usuario """

    def get(self):
        """ Método de Obtención de toda la Experiencia laboral de un Usuario """
        user_work = db_session.query(Work).filter(Work.user_email == current_user.email).all()

        return work_schema.dump(user_work, many=True)
