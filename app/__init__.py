"""Archivo que crea la Aplicación de Flask"""
from uuid import uuid4
from flask import Flask


def create_app():
    """Crea la Aplicación de Flask"""
    app = Flask(__name__, static_folder='static', template_folder='view')
    app.env = 'development'
    app.config['SECRET_KEY'] = uuid4().hex

    return app
    