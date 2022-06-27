"""Fichero para la creación del formulario de inicio"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Email, Length, ValidationError
from app.utils.hash_password import check_password
from app.model.user import User
from app.model.db_config import db_session

class LoginForm(FlaskForm):
    """Clase para la realización del formulario de inicio"""
    email = StringField('Correo', [
                                    InputRequired(), 
                                    Length(min=6, max=60), 
                                    Email(message="El email no es válido")
                                    ])
    password = PasswordField('Contraseña', [
                                            DataRequired()
                                            ])

    def validate_email(self,email):
        """Función que valida el email"""

        user_email = db_session.query(User).filter_by(email=email.data).first()

        if user_email:
            raise ValidationError(f'El email {email.data} ya existe')

    btn_continue = SubmitField('Continuar')
    