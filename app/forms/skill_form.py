""" Formulario para añadir habilidades """
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerRangeField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class SkillForm(FlaskForm):

    """ Clase que representa el formulario para añadir habilidades """

    name = StringField('Hobby', validators=[
                       DataRequired(message="La habilidad es requerida")])

    level = IntegerRangeField('Nivel', validators=[DataRequired(message="El nivel es requerido"), NumberRange(
        min=1, max=10, message="El nivel debe estar entre 1 y 10")])

    submit = SubmitField('Añadir')
