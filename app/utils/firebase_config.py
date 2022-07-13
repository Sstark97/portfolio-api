""" Archivo para configurar la app Firebase """
from os import getenv
from dotenv import load_dotenv
from pyrebase import initialize_app

load_dotenv()

config = {
    'apiKey': getenv('FIRE_BASE_API_KEY'),
    'authDomain': getenv('FIRE_BASE_AUTH_DOMAIN'),
    'databaseURL': getenv('FIRE_BASE_DATABASE_URL'),
    'projectId': getenv('FIRE_BASE_PROJECT_ID'),
    'storageBucket': getenv('FIRE_BASE_STORAGE_BUCKET'),
    'messagingSenderId': getenv('FIRE_BASE_MESSAGING_SENDER_ID'),
    'appId': getenv('FIRE_BASE_APP_ID'),
    'measurementId': getenv('FIRE_BASE_MEASUREMENT_ID')
}

firebase = initialize_app(config)
storage = firebase.storage()
