""" Controlador para manejar la cuenta del usuario"""
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from app.forms.register_form import RegisterForm

account = Blueprint('account', __name__)

@account.route('/account')
@login_required
def about():
    """Página de Acerca de"""
    form = RegisterForm()

    return render_template('account.html', form=form)
    