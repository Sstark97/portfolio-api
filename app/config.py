""" Archivo de Configuración de la App de Flask"""
from os import getenv
from dotenv import load_dotenv

class Config:
    """Clase con la configuración de la Aplicación de Flask"""
    load_dotenv()

    SECRET_KEY = getenv('SECRET_KEY')
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///portfolio.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'static/img'
    