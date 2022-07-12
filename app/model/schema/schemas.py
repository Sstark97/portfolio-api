""" Módulo con todos los esquemas de la App """
from app.model.schema.schema_config import ma
from app.model.models import User
from app.model.schema.education_schema import education_schema, EducationSchema
from app.model.schema.hobbies_schema import hobbies_schema, HobbieSchema
from app.model.schema.skills_schema import skills_schema, SkillSchema
from app.model.schema.work_schema import work_schema, WorkSchema
from app.model.schema.project_schema import project_schema, ProjectSchema

class UserSchema(ma.SQLAlchemySchema):
    """ Esquema de los Proyectos de un Usuario """

    class Meta:
        """ Meta """
        model = User
    
    email = ma.auto_field()
    name = ma.auto_field()
    surname = ma.auto_field()
    presentation = ma.auto_field()
    adress = ma.auto_field()
    phone = ma.auto_field()
    avatar = ma.auto_field()
    hobbies = ma.Nested(HobbieSchema, many=True)
    skills = ma.Nested(SkillSchema, many=True)
    works = ma.Nested(WorkSchema, many=True)
    education = ma.Nested(EducationSchema, many=True)
    project = ma.Nested(ProjectSchema, many=True)

user_schema = UserSchema()
