""" Formulario para añadir hobbies """
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class HobbyForm(FlaskForm):
    
    """ Clase que representa el formulario para añadir hobbies """

    name = StringField('Hobby', validators=[DataRequired(message="El hobby es requerido")])

    submit = SubmitField('Añadir')
