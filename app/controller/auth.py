"""Blueprint que se encarga de la autenticación de los usuarios"""
from flask import Blueprint, render_template
from app.forms.register_form import RegisterForm

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login_index():
    """Página de Login"""

    return "Login"

@auth.route('/register', methods=['GET', 'POST'])
def register_index():
    """Página de Registro"""

    register_form = RegisterForm()

    context = {
        'title': 'Registro',
        'form': register_form
    }

    if register_form.validate_on_submit():
        print("DDD")

    return render_template('auth.html', **context)

@auth.route('/logout')
def logout_index():
    """Página de Logout"""
    return "Logout"
