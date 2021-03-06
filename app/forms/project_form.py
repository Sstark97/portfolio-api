""" Modulo con el formulario de Proyectos """
from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, SubmitField, FileField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError
from app.model.db_config import db_session
from app.model.models import Project

class ProjectForm(FlaskForm):
    """ Formulario de los Proyectos """
    name = StringField('Nombre', validators=[
    DataRequired(message="El nombre es requerido"),
    Length(min=3, max=20, message="El nombre debe tener entre 3 y 20 caracteres")])
    
    description = TextAreaField('Descripción', [Length(min=10, max=1000)])

    project_img = FileField('Imagen', render_kw={'accept':'image/png, image/jpeg'})

    web = StringField('Web', [Length(min=0, max=100)])

    repository = StringField('Repositorio', [Length(min=3, max=100), DataRequired(message="El Repositorio es requerido")])

    submit = SubmitField('Crear')
