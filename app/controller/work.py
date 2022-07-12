""" Controlador para manejar la experiencia de trabajo de un usuario """
from datetime import date
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app.forms.forms import WorkForm, DeleteDataForm
from app.model.db_config import db_session
from app.model.models import Work

work = Blueprint('work', __name__)


@work.route('/work', methods=['GET', 'POST'])
@login_required
def work_index():
    """ Página de Acerca de """

    user_works = db_session.query(Work).filter_by(user_email=current_user.email).all()
    work_fields = ['position', 'company', 'description', 'start_date', 'final_date', 'current']

    context = {
        'title': 'Experiencia de Trabajo',
        'type': 'Experiencia de Trabajo',
        'message': 'No hay Experiencia de Trabajo, añada una nueva',
        'action': url_for('work.work_new'),
        'delete_action': '/work/delete/',
        'edit_action': '/work/edit/',
        'data': user_works,
        'fields': work_fields,
    }

    return render_template('data.html', **context)


@work.route('/work/new', methods=['GET', 'POST'])
@login_required
def work_new():
    """ Página de creación de experiencia de trabajo """

    work_form = WorkForm()

    context = {
        'title': 'Nueva Experiencia de Trabajo',
        'form': work_form,
        'action': url_for('work.work_new')
    }

    if work_form.validate_on_submit():
        start_date = date(work_form.start_date.data.year,
                          work_form.start_date.data.month, work_form.start_date.data.day)
        final_date = None
        current = True

        if work_form.final_date.data:
            final_date = date(work_form.final_date.data.year,
                              work_form.final_date.data.month, work_form.final_date.data.day)
            current = False

        new_work = Work(position=work_form.position.data, company=work_form.company.data, description=work_form.description.data,
                    start_date=start_date, final_date=final_date, current=current, user_email=current_user.email)
        
        db_session.add(new_work)
        db_session.commit()

        return redirect(url_for('work.work_index'))
    
    return render_template('forms.html', **context)

@work.route('/work/edit/<int:work_id>', methods=['GET', 'POST'])
@login_required
def work_edit(work_id):
    """ Página de edición de experiencia de trabajo """

    work_to_edit = db_session.query(Work).filter_by(id=work_id).first()

    work_form = WorkForm(request.form) if request.method == 'POST' else WorkForm(obj=work_to_edit)
    work_form.submit.label.text = 'Editar'

    context = {
        'title': 'Editar Experiencia de Trabajo',
        'form': work_form,
        'action': url_for('work.work_edit', work_id=work_id),
        'data': work_to_edit,
    }

    if work_form.validate_on_submit():
        start_date = date(work_form.start_date.data.year,
                          work_form.start_date.data.month, work_form.start_date.data.day)
        final_date = None
        current = True

        if work_form.final_date.data:
            final_date = date(work_form.final_date.data.year,
                              work_form.final_date.data.month, work_form.final_date.data.day)
            current = False

        work_to_edit.position = work_form.position.data
        work_to_edit.company = work_form.company.data
        work_to_edit.description = work_form.description.data
        work_to_edit.start_date = start_date
        work_to_edit.final_date = final_date
        work_to_edit.current = current
        db_session.commit()

        return redirect(url_for('work.work_index'))

    return render_template('forms.html', **context)

@work.route('/work/delete/<int:work_id>', methods=['GET', 'POST'])
@login_required
def work_delete(work_id):
    """ Página de eliminación de experiencia de trabajo """

    work_to_delete = db_session.query(Work).filter_by(id=work_id).first()
    delete_form = DeleteDataForm()

    context = {
        'title': 'Eliminar Experiencia de Trabajo',
        'type': 'Experiencia de Trabajo',
        'name': work_to_delete.position,
        'delete': True,
        'data': work_to_delete,
        'form': delete_form,
        'action': url_for('work.work_delete', work_id=work_id),

    }

    if request.method == 'POST':
        db_session.delete(work_to_delete)
        db_session.commit()

        return redirect(url_for('work.work_index'))

    return render_template('forms.html', **context)
