""" Archivo de Configuración de la App de Flask"""
from uuid import uuid4

class Config:
    """Clase con la configuración de la Aplicación de Flask"""

    SECRET_KEY = uuid4().hex
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
