""" Controlador para manejar la experiencia de trabajo de un usuario """
from datetime import datetime, date
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app.forms.forms import WorkForm
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
        final_date = date(work_form.final_date.data.year,
                          work_form.final_date.data.month, work_form.final_date.data.day)

        new_work = Work(position=work_form.position.data, company=work_form.company.data, description=work_form.description.data,
                    start_date=start_date, final_date=final_date, current=work_form.current.data, user_email=current_user.email)
        
        db_session.add(new_work)
        db_session.commit()

        return redirect(url_for('work.work_index'))
    
    return render_template('forms.html', **context)
