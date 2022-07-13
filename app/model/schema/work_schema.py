""" Esquema de la Experiencia Laboral de un Usuario """
from app.model.schema.schema_config import ma
from app.model.models import Work

class WorkSchema(ma.SQLAlchemySchema):
    """ Esquema de la experiencia laboral de un Usuario """

    class Meta:
        """ Meta """
        model = Work
    
    position = ma.auto_field()
    company = ma.auto_field()
    description = ma.auto_field()
    start_date = ma.auto_field()
    final_date = ma.auto_field()
    current = ma.auto_field()

work_schema = WorkSchema()
