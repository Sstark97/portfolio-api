""" Esquema de los Proyectos de un Usuario """
from app.model.schema.schema_config import ma
from app.model.models import Project

class ProjectSchema(ma.SQLAlchemySchema):
    """ Esquema de los Proyectos de un Usuario """

    class Meta:
        """ Meta """
        model = Project
    
    name = ma.auto_field()
    description = ma.auto_field()
    image = ma.auto_field()
    web = ma.auto_field()
    repository = ma.auto_field()

project_schema = ProjectSchema()
