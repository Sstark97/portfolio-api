""" Ruta para las Habilidades de un Usuario """
from flask_restful import Resource
from flask_login import current_user
from app.model.db_config import db_session
from app.model.models import Skill
from app.model.schema.schemas import skills_schema

class Skills(Resource):
    """ Recurso para obtener las Habilidades de un Usuario """

    def get(self):
        """ Método de Obtención de las Habilidades de un Usuario """
        user_skills = db_session.query(Skill).filter(Skill.user_email == current_user.email).all()

        return skills_schema.dump(user_skills, many=True)
