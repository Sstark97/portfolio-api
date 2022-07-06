""" Formulario para añadir experiencia laboral """
from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Optional, ValidationError

class WorkForm(FlaskForm):

    """ Clas que representa el formulario para añadir experiencia laboral """

    position = StringField('Puesto de Trabajo', validators=[DataRequired(message="El puesto de trabajo es requerido")])

    company = StringField('Empresa', validators=[DataRequired(message="La empresa es requerida")])

    description = TextAreaField('Descripción')

    start_date = DateField('Fecha de Inicio', validators=[DataRequired(message="La fecha de inicio es requerida")])

    final_date = DateField('Fecha de Finalización', validators=[Optional()])

    def validate_final_date(self,final_date):
        """ Función que valida que la fecha de finalización sea mayor que la de inicio """
        if isinstance(final_date.data,date) and self.start_date.data > final_date.data:
            raise ValidationError("La fecha de finalización debe ser mayor que la de inicio")

    submit = SubmitField('Añadir')
