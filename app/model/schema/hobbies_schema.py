""" Esquema de las Habilidades de un Usuario """
from app.model.schema.schema_config import ma
from app.model.models import Hobby

class HobbieSchema(ma.SQLAlchemySchema):
    """ Esquema de las Habilidades de un Usuario """

    class Meta:
        """ Meta """
        model = Hobby
    
    name = ma.auto_field()

hobbies_schema = HobbieSchema()
