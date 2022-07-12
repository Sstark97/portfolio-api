""" Archivo con decoradores custom """
from flask import redirect, url_for
from flask_login import current_user

def login_redirect(func):
    """ Redirecciona a la página de inicio si no está logueado """
    def wrapper(*args, **kwargs):
    
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        return func(*args, **kwargs)

    wrapper.__name__ = func.__name__  
    return wrapper
