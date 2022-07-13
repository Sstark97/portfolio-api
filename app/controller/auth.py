""" Controlador que se encarga de la autenticación de los usuarios """
from secrets import token_hex
from os import getenv
from dotenv import load_dotenv
from jwt import encode
from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_user, login_required, logout_user
from app.utils.hash_password import hash_password, check_password
from app.utils.firebase_config import storage
from app.utils.decorators import login_redirect
from app.forms.forms import RegisterForm, LoginForm
from app.model.db_config import db_session
from app.model.models import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
@login_redirect
def login():
    """Página de Login"""

    login_form = LoginForm()

    context = {
        'title': 'inicio de Sesión',
        'form_title': 'Inicio de Sesión',
        'form': login_form,
        'action': url_for('auth.login')
    }

    if login_form.validate_on_submit():
        user = db_session.query(User).filter_by(
            email=login_form.email.data).first()

        if check_password(login_form.password.data, user.password):

            login_user(user, remember=login_form.remember_me.data)
            return redirect(url_for('index'))

        return render_template('forms.html', **context)

    return render_template('forms.html', **context)

@auth.route('/register', methods=['GET', 'POST'])
@login_redirect
def register():
    """Página de Registro"""

    register_form = RegisterForm()

    context = {
        'title': 'Registro',
        'form_title': 'Formulario de Registro',
        'form': register_form,
        'action': url_for('auth.register')
    }

    if register_form.validate_on_submit():
        user_avatar = register_form.avatar.data if register_form.avatar.data else None
        user_avatar_path = None

        if user_avatar:
            storage.child(f'users/{register_form.email.data}/avatar').put(user_avatar)
            user_avatar_path = storage.child(f'users/{register_form.email.data}/avatar').get_url(token=token_hex(16))
        
        load_dotenv()
        token = encode({ 'public_id': register_form.name.data }, getenv('SECRET_KEY'))

        new_user = User(register_form.email.data, register_form.name.data, register_form.surnames.data, register_form.adress.data,
                        register_form.phone.data, hash_password(register_form.password.data), token, 
                        presentation=register_form.presentation.data, avatar=user_avatar_path)
        db_session.add(new_user)
        db_session.commit()

        login_user(new_user, remember=True)

        return redirect(url_for('index'))

    return render_template('forms.html', **context)

@auth.route('/logout')
@login_required
def logout_index():
    """Ruta de Logout"""

    logout_user()
    return redirect(url_for('index'))
