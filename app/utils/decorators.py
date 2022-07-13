""" Archivo con decoradores custom """
from flask import redirect, url_for, request, jsonify
from flask_login import current_user
from app.model.db_config import db_session
from app.model.models import User

def login_redirect(func):
    """ Redirecciona a la página de inicio si no está logueado """
    def wrapper(*args, **kwargs):
    
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        return func(*args, **kwargs)

    wrapper.__name__ = func.__name__  
    return wrapper

def token_required(func):
    """ Verifica que exista un token en la petición """
    def wrapper(*args, **kwargs):

        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
            db_token = db_session.query(User).filter(User.api_token == token).first()

            if not db_token:
                return jsonify({'message': 'Invalid token'})

        if not token:
            return jsonify({'message': 'a valid token is missing'})
        
        return func(*args, **kwargs)
    
    wrapper.__name__ = func.__name__  
    return wrapper
