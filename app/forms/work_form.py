""" Formulario para añadir experiencia laboral """
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, ValidationError

class WorkForm(FlaskForm):

    """ Clas que representa el formulario para añadir experiencia laboral """

    position = StringField('Puesto de Trabajo', validators=[DataRequired(message="El puesto de trabajo es requerido")])

    company = StringField('Empresa', validators=[DataRequired(message="La empresa es requerida")])

    description = TextAreaField('Descripción')

    start_date = DateField('Fecha de Inicio', validators=[DataRequired(message="La fecha de inicio es requerida")])

    final_date = DateField('Fecha de Finalización')

    def validate_final_date(self,final_date):
        """ Función que valida que la fecha de finalización sea mayor que la de inicio """
        if final_date.data and self.start_date.data > final_date.data:
            raise ValidationError("La fecha de finalización debe ser mayor que la de inicio")

    current = BooleanField('Actual')

    submit = SubmitField('Añadir')
