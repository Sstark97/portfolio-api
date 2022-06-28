"""Blueprint que se encarga de la autenticación de los usuarios"""
from secrets import token_hex
from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_user, login_required, logout_user
from app.utils.hash_password import hash_password, check_password
from app.forms.register_form import RegisterForm
from app.forms.login_form import LoginForm
from app.model.db_config import db_session
from app.model.user import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login_index():
    """Página de Login"""

    login_form = LoginForm()

    context = {
        'title': 'inicio de Sesión',
        'form_title': 'Inicio de Sesión',
        'form': login_form
    }

    if login_form.validate_on_submit():
        user= db_session.query(User).filter_by(email=login_form.email.data).first()

        if check_password(login_form.password.data, user.password):
  
            login_user(user, remember=login_form.remember_me.data)
            return redirect(url_for('index'))
        
        return render_template('auth.html', **context)

    return render_template('auth.html', **context)

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
                        register_form.phone.data, hash_password(register_form.password.data), token_hex(16))
        db_session.add(new_user)
        db_session.commit()

        login_user(new_user, remember=True)

        return redirect(url_for('index'))

    return render_template('auth.html', **context)

@auth.route('/logout')
@login_required
def logout_index():
    """Ruta de Logout"""

    logout_user()
    return redirect(url_for('index'))
