"""Fichero para la creación del formulario de inicio"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, InputRequired, Email, Length, ValidationError
from app.utils.hash_password import check_password
from app.model.models import User
from app.model.db_config import db_session

class LoginForm(FlaskForm):
    """Clase para la realización del formulario de inicio"""
    email = StringField('Correo', [
        InputRequired(),
        Length(min=6, max=60),
        Email(message="El email no es válido")
    ])

    def validate_email(self, email):
        """Función que valida el email"""

        user_email = db_session.query(User).filter_by(email=email.data).first()

        if not user_email:
            raise ValidationError(f'El email {email.data} no existe')
    
    password = PasswordField('Contraseña', [
        DataRequired()
    ])

    def validate_password(self,password):
        """Función que valida la contraseña"""

        passwd_db = db_session.query(User).filter_by(email=self.email.data).first()
        passwd = passwd_db.password if passwd_db else None
        
        if passwd and not check_password(password.data, passwd):
            raise ValidationError('La contraseña no es valida')


    remember_me = BooleanField('Recordarme')

    submit = SubmitField('Continuar')
