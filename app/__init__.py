from flask import Flask
from uuid import uuid4

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='view')
    app.env = 'development'
    app.config['SECRET_KEY'] = uuid4().hex

    return app