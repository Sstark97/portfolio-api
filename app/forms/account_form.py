""" Modulo con el formulario de Registro de Usuarios """
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, regexp

class AccountForm(FlaskForm):
    """ Formulario para cambiar los datos de la cuenta """

    name = StringField('Nombre', validators=[
        DataRequired(message="El nombre es requerido"),
        Length(min=3, max=20, message="El nombre debe tener entre 3 y 20 caracteres")])

    surname = StringField('Apellidos', validators=[Length(
        min=3, max=30, message="El apellido debe tener entre 3 y 20 caracteres")])
    
    presentation = TextAreaField('Presentación', [Length(min=10, max=1000)])

    adress = StringField('Direccion', validators=[Length(
        min=3, max=100, message="La direccion debe tener entre 3 y 100 caracteres")])

    phone = StringField('Telefono', validators=[Length(
        min=9, max=9, message="El telefono debe tener 9 caracteres"), regexp('[0-9]+', message="El número debe contener solo digitos")])

    password = PasswordField('Contraseña', validators=[ EqualTo('password_confirm',
                                                                                          message='Las contraseñas no coinciden')])

    password_confirm = PasswordField('Repita la contraseña', [Length(max=20)])

    avatar = FileField('Avatar', render_kw={'accept': 'image/png, image/jpeg'})

    submit = SubmitField('Guardar')
