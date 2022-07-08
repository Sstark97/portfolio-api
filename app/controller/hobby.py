""" Controlador para manejar los hobbies de un usuario """
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app.forms.forms import HobbyForm, DeleteDataForm
from app.model.db_config import db_session
from app.model.models import Hobby

hobby = Blueprint('hobby', __name__)

@hobby.route('/hobby', methods=['GET', 'POST'])
@login_required
def hobby_index():
    """ Página de Acerca de """

    user_hobbies = db_session.query(Hobby).filter_by(
        user_email=current_user.email).all()
    hobby_fields = ['name']

    context = {
        'title': 'Datos Académicos',
        'type': 'Datos Académicos',
        'action': url_for('hobby.hobby_new'),
        'delete_action': '/hobby/delete/',
        'edit_action': '/hobby/edit/',
        'data': user_hobbies,
        'fields': hobby_fields,
    }

    return render_template('data.html', **context)

@hobby.route('/hobby/new', methods=['GET', 'POST'])
@login_required
def hobby_new():
    """ Página de creación de Hobbies """

    hobby_form = HobbyForm()

    context = {
        'title': 'Nuevo Hobby',
        'form': hobby_form,
        'action': url_for('hobby.hobby_new')
    }

    if hobby_form.validate_on_submit():

        new_hobby = Hobby(name=hobby_form.name.data, user_email=current_user.email)

        db_session.add(new_hobby)
        db_session.commit()

        return redirect(url_for('hobby.hobby_index'))

    return render_template('forms.html', **context)

@hobby.route('/hobby/edit/<int:hobby_id>', methods=['GET', 'POST'])
@login_required
def hobby_edit(hobby_id):
    """ Página de edición de Hobbies """

    hobby_data = db_session.query(Hobby).filter_by(id=hobby_id).first()

    if request.method == 'POST':
        hobby_form = HobbyForm(request.form)
    else:
        hobby_form = HobbyForm()
        hobby_form.name.data = hobby_data.name

    context = {
        'title': 'Editar Hobby',
        'form': hobby_form,
        'action': url_for('hobby.hobby_edit', hobby_id=hobby_id),
        'data': hobby_data,
    }

    if hobby_form.validate_on_submit():

        hobby_data.name = hobby_form.name.data
        db_session.commit()

        return redirect(url_for('hobby.hobby_index'))

    return render_template('forms.html', **context)
