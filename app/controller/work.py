""" Controlador para manejar la experiencia de trabajo de un usuario """
from secrets import token_hex
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, logout_user, current_user
from app.forms.forms import AccountForm, DeleteAccountForm
from app.model.db_config import db_session
from app.model.models import Work

work = Blueprint('work', __name__)

@work.route('/work', methods=['GET', 'POST'])
@login_required
def work_index():
    """ Página de Acerca de """

    context = {
        'title': 'Experiencia de Trabajo',
        'action': url_for('work.work_index'),
        'type': 'work',
        'type_name': 'Experiencia de Trabajo',
        'cv': False,
        'form': ""
    }

    return render_template('forms.html', **context)
