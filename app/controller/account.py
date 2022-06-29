""" Controlador para manejar la cuenta del usuario"""
from secrets import token_hex
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, logout_user, current_user
from app.forms.forms import AccountForm, DeleteAccountForm
from app.utils.hash_password import hash_password
from app.utils.firebase_config import storage
from app.model.db_config import db_session
from app.model.models import User

account = Blueprint('account', __name__)

@account.route('/account', methods=['GET', 'POST'])
@login_required
def profile():
    """Página de Acerca de"""
    if request.method == 'POST':
        form = AccountForm(request.form)
    else: 
        form = AccountForm()
        form.name.data = current_user.name
        form.surnames.data = current_user.surname
        form.adress.data = current_user.adress
        form.phone.data = current_user.phone

    context = {
        'form': form,
        'action': url_for('account.profile'),
        'token_action': url_for('account.token'),
    }

    if form.validate_on_submit():
        avatar_path = None
        user_avatar = request.files.get('avatar') if request.files.get('avatar') else None

        if user_avatar:
            storage.delete(f'users/{current_user.email}/avatar', token=token_hex(16))
            storage.child(f'users/{current_user.email}/avatar').put(user_avatar)
            avatar_path = storage.child(f'users/{current_user.email}/avatar').get_url(token=token_hex(16))

        db_session.query(User).filter(User.email == current_user.email).update(
            {
                'name': form.name.data,
                'surname': form.surnames.data,
                'adress': form.adress.data,
                'phone': form.phone.data,
                'password': hash_password(form.password.data) if form.password.data else current_user.password,
                'avatar': avatar_path if avatar_path else current_user.avatar
            }
        )
        db_session.commit()
        return redirect(url_for('account.profile'))


    return render_template('account.html', **context)

@account.route('/account/generate_token', methods=['GET', 'POST'])
@login_required
def token():
    """Genera un token de acceso para el usuario"""
    new_token = token_hex(16)
    db_session.query(User).filter(User.email == current_user.email).update( {'api_token': new_token} )
    db_session.commit()

    return redirect(url_for('account.profile'))

@account.route('/account/delete', methods=['GET', 'POST'])
@login_required
def delete_account():
    """Página de Eliminación de la Cuenta"""
    form = DeleteAccountForm()

    if form.validate_on_submit():
        storage.delete(f'users/{current_user.email}/avatar', token=token_hex(16))
        db_session.query(User).filter(User.email == current_user.email).delete()
        db_session.commit()
        logout_user()

        return redirect(url_for('index'))

    return render_template('delete_account.html', form=form)
