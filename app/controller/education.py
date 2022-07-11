""" Controlador para manejar la Datos Académicos de un usuario """
from datetime import date
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app.forms.forms import EducationForm, DeleteDataForm
from app.model.db_config import db_session
from app.model.models import Education

education = Blueprint('education', __name__)


@education.route('/education', methods=['GET', 'POST'])
@login_required
def education_index():
    """ Página de Acerca de """

    user_educations = db_session.query(Education).filter_by(
        user_email=current_user.email).all()
    education_fields = ['study', 'education_institution',
                        'description', 'start_date', 'final_date', 'current', 'course']

    context = {
        'title': 'Datos Académicos',
        'type': 'Datos Académicos',
        'action': url_for('education.education_new'),
        'delete_action': '/education/delete/',
        'edit_action': '/education/edit/',
        'data': user_educations,
        'fields': education_fields,
    }

    return render_template('data.html', **context)


@education.route('/education/new', methods=['GET', 'POST'])
@login_required
def education_new():
    """ Página de creación de Datos Académicos """

    education_form = EducationForm()

    context = {
        'title': 'Nueva Datos Académicos',
        'form': education_form,
        'action': url_for('education.education_new')
    }

    if education_form.validate_on_submit():
        start_date = date(education_form.start_date.data.year,
                          education_form.start_date.data.month, education_form.start_date.data.day)
        final_date = None
        current = False

        if education_form.final_date.data:
            final_date = date(education_form.final_date.data.year,
                              education_form.final_date.data.month, education_form.final_date.data.day)
            current = True

        new_education = Education(study=education_form.study.data, education_institution=education_form.education_institution.data, 
                                    description=education_form.description.data, start_date=start_date, final_date=final_date, 
                                    current=current, course=education_form.course.data, user_email=current_user.email)

        db_session.add(new_education)
        db_session.commit()

        return redirect(url_for('education.education_index'))

    return render_template('forms.html', **context)


@education.route('/education/edit/<int:education_id>', methods=['GET', 'POST'])
@login_required
def education_edit(education_id):
    """ Página de edición de Datos Académicos """

    education_to_edit = db_session.query(
        Education).filter_by(id=education_id).first()
    
    education_form = education_form = EducationForm(request.form) if request.method == 'POST' else EducationForm(obj=education_to_edit)
    education_form.submit.label.text = 'Editar'

    context = {
        'title': 'Editar Datos Académicos',
        'form': education_form,
        'action': url_for('education.education_edit', education_id=education_id),
        'data': education_to_edit,
    }

    if education_form.validate_on_submit():
        start_date = date(education_form.start_date.data.year,
                          education_form.start_date.data.month, education_form.start_date.data.day)
        final_date = None
        current = False

        if education_form.final_date.data:
            final_date = date(education_form.final_date.data.year,
                              education_form.final_date.data.month, education_form.final_date.data.day)
            current = True

        education_to_edit.study = education_form.study.data
        education_to_edit.education_institution = education_form.education_institution.data
        education_to_edit.description = education_form.description.data
        education_to_edit.start_date = start_date
        education_to_edit.final_date = final_date
        education_to_edit.current = current
        education_to_edit.course = education_form.course.data
        db_session.commit()

        return redirect(url_for('education.education_index'))

    return render_template('forms.html', **context)


@education.route('/education/delete/<int:education_id>', methods=['GET', 'POST'])
@login_required
def education_delete(education_id):
    """ Página de eliminación de Datos Académicos """

    education_to_delete = db_session.query(Education).filter_by(id=education_id).first()
    delete_form = DeleteDataForm()

    context = {
        'title': 'Eliminar Datos Académicos',
        'type': 'Datos Académicos',
        'name': education_to_delete.study,
        'delete': True,
        'data': education_to_delete,
        'form': delete_form,
        'action': url_for('education.education_delete', education_id=education_id),

    }

    if request.method == 'POST':
        db_session.delete(education_to_delete)
        db_session.commit()

        return redirect(url_for('education.education_index'))

    return render_template('forms.html', **context)
