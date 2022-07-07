""" Formulario para añadir datos academicos """
from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, TextAreaField, IntegerRangeField
from wtforms.validators import DataRequired, Optional, ValidationError

class EducationForm(FlaskForm):

    """ Clase que representa el formulario para añadir datos academicos """

    study = StringField('Estudio', validators=[DataRequired(message="El estudio es requerido")])

    education_institution = StringField('Institución Académica', validators=[DataRequired(message="La Institución Académica es requerida")])

    description = TextAreaField('Descripción')

    start_date = DateField('Fecha de Inicio', validators=[DataRequired(message="La fecha de inicio es requerida")])

    final_date = DateField('Fecha de Finalización', validators=[Optional()])

    def validate_final_date(self,final_date):
        """ Función que valida que la fecha de finalización sea mayor que la de inicio """
        if isinstance(final_date.data,date) and self.start_date.data > final_date.data:
            raise ValidationError("La fecha de finalización debe ser mayor que la de inicio")

    course = IntegerRangeField('Curso', validators=[DataRequired(message="El curso es requerido")], min=1, max=10)

    submit = SubmitField('Añadir')
