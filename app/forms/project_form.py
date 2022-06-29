""" Modulo con el formulario de Proyectos """
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError
from app.model.db_config import db_session
from app.model.models import Project

class ProjectForm(FlaskForm):
    """ Formulario de los Proyectos """
    name = StringField('Nombre', validators=[
    DataRequired(message="El nombre es requerido"),
    Length(min=3, max=20, message="El nombre debe tener entre 3 y 20 caracteres")])

    def validate_name(self,name):
        """ Función que valida que el nombre de un Proyecto no este repetido """
        proyect_name = db_session.query(Project).filter_by(name=name.data).first()

        if proyect_name:
            raise ValidationError(f'El nombre {name.data} ya existe')
    
    description = TextAreaField('Sinopsis', [Length(min=10, max=1000)])

    project_img = FileField('Imagen del Proyecto', render_kw={'accept':'image/png, image/jpeg'})

    submit = SubmitField('Crear')
