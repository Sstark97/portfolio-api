"""Blueprint que se encarga de la autenticación de los usuarios"""
from secrets import token_hex
from flask import Blueprint, redirect, render_template, url_for
from app.forms.register_form import RegisterForm
from app.model.db_config import db_session
from app.model.user import User

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
        'form_title': 'Formulario de Registro',
        'form': register_form
    }

    if register_form.validate_on_submit():
        new_user = User( register_form.email.data, register_form.name.data, register_form.surname.data, register_form.adress.data,
                        register_form.phone.data, register_form.password.data, token_hex(16))
        db_session.add(new_user)
        db_session.commit()

        return redirect(url_for('index'))

    return render_template('auth.html', **context)


@auth.route('/logout')
def logout_index():
    """Página de Logout"""
    return "Logout"
