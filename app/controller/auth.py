"""Blueprint que se encarga de la autenticación de los usuarios"""
from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login_index():
    """Página de Login"""
    return "Login"

@auth.route('/register')
def register_index():
    """Página de Registro"""
    return "Register"

@auth.route('/logout')
def logout_index():
    """Página de Logout"""
    return "Logout"
    