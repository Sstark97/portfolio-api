""" Modulo con el formulario de Registro de Usuarios """
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, Length, ValidationError, regexp
from app.model.db_config import db_session
from app.model.user import User

class RegisterForm(FlaskForm):
    """ Formulario de Registro de Usaurios """
    email = EmailField('Email', validators=[DataRequired(
        message="El email es requerido"), Email(message="El email no es valido")])
    
    def validate_email(self,email):
        """Función que valida el email"""
        user_email = db_session.query(User).filter_by(email=email.data).first()

        if user_email:
            raise ValidationError(f'El email {email.data} ya existe')

    name = StringField('Nombre', validators=[
        DataRequired(message="El nombre es requerido"),
        Length(min=3, max=20, message="El nombre debe tener entre 3 y 20 caracteres")])

    surnames = StringField('Apellidos', validators=[Length(
        min=3, max=30, message="El apellido debe tener entre 3 y 20 caracteres")])

    adress = StringField('Direccion', validators=[Length(
        min=3, max=100, message="La direccion debe tener entre 3 y 100 caracteres")])

    phone = StringField('Telefono', validators=[Length(
        min=9, max=9, message="El telefono debe tener 9 caracteres"), regexp('[0-9]+', message="El número debe contener solo digitos")])

    password = PasswordField('Contraseña', validators=[DataRequired("El password es requerido"), Length(
        min=6, max=20, message="El password debe tener entre 6 y 20 caracteres")])
    
    avatar = FileField('Avatar', render_kw={'accept':'image/png, image/jpeg'})
    
    submit = SubmitField('Registrar')
