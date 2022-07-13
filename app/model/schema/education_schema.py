""" Esquema de los Datos Académicos de un Usuario """
from app.model.schema.schema_config import ma
from app.model.models import Education

class EducationSchema(ma.SQLAlchemySchema):
    """ Esquema de los Datos Académicos de un Usuario """

    class Meta:
        """ Meta """
        model = Education
    
    study = ma.auto_field()
    education_institution = ma.auto_field()
    description = ma.auto_field()
    start_date = ma.auto_field()
    final_date = ma.auto_field()
    current = ma.auto_field()
    course = ma.auto_field()

education_schema = EducationSchema()
