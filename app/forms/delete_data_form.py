"""Formulario de Eliminacion de Contenido"""
from flask_wtf import FlaskForm
from wtforms import SubmitField 

class DeleteDataForm(FlaskForm):
    """Clase para el formulario de Eliminación de Datos"""

    submit = SubmitField(render_kw={'value':'Borrar', 'class':'btn btn_danger'})
