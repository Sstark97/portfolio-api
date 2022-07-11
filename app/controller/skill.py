""" Controlador para manejar las habilidades de un usuario """
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app.forms.forms import SkillForm, DeleteDataForm
from app.model.db_config import db_session
from app.model.models import Skill

skill = Blueprint('skills', __name__)

@skill.route('/skills', methods=['GET', 'POST'])
@login_required
def skills_index():
    """ Página de Acerca de """

    user_skills = db_session.query(Skill).filter_by(
        user_email=current_user.email).all()
    skills_fields = ['name', 'level']

    context = {
        'title': 'Habilidades',
        'type': 'Habilidades',
        'action': url_for('skills.skills_new'),
        'delete_action': '/skills/delete/',
        'edit_action': '/skills/edit/',
        'data': user_skills,
        'fields': skills_fields,
    }

    return render_template('data.html', **context)

@skill.route('/skills/new', methods=['GET', 'POST'])
@login_required
def skills_new():
    """ Página de creación de skills """

    skills_form = SkillForm()

    context = {
        'title': 'Nueva Habilidad',
        'form': skills_form,
        'action': url_for('skills.skills_new')
    }

    if skills_form.validate_on_submit():

        new_skills = Skill(name=skills_form.name.data, level=skills_form.level.data, user_email=current_user.email)

        db_session.add(new_skills)
        db_session.commit()

        return redirect(url_for('skills.skills_index'))

    return render_template('forms.html', **context)

@skill.route('/skills/edit/<int:skill_id>', methods=['GET', 'POST'])
@login_required
def skills_edit(skill_id):
    """ Página de edición de skills """

    skill_data = db_session.query(Skill).filter_by(id=skill_id).first()
    if request.method == 'POST':
        skills_form = SkillForm(request.form)
    else:
        skills_form = SkillForm(obj=skill_data)
        skills_form.submit.label.text = 'Editar'

    context = {
        'title': 'Editar Habilidad',
        'form': skills_form,
        'action': url_for('skills.skills_edit', skill_id=skill_id),
        'data': skill_data,
    }

    if skills_form.validate_on_submit():

        skill_data.name = skills_form.name.data
        skill_data.level = skills_form.level.data

        db_session.commit()

        return redirect(url_for('skills.skills_index'))

    return render_template('forms.html', **context) 
