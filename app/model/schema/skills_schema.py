""" Esquema de las Habilidades de un Usuario """
from app.model.schema.schema_config import ma
from app.model.models import Skill

class SkillSchema(ma.SQLAlchemySchema):
    """ Esquema de las Habilidades de un Usuario """

    class Meta:
        """ Meta """
        model = Skill
    
    name = ma.auto_field()
    level = ma.auto_field()

skills_schema = SkillSchema()
