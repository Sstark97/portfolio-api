"""Formulario de Eliminacion de la Cuenta"""
from flask_wtf import FlaskForm
from wtforms import SubmitField, EmailField
from wtforms.validators import InputRequired, Email, ValidationError
from flask_login import current_user

class DeleteAccountForm(FlaskForm):
    """Clase para el formulario de Eliminación de una Cuenta"""

    email = EmailField('Email', [InputRequired(), Email()])

    def validate_email(self, email):
        """Función para validar el email"""

        if email.data != current_user.email:
            raise ValidationError('El email no coincide')

    submit = SubmitField('Eliminar Cuenta')
