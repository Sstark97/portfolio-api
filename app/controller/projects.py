""" Controlador que se encarga de la autenticación de los proyectos de un usuario """
from dataclasses import fields
from secrets import token_hex
from flask import Blueprint, redirect, render_template, url_for
from flask_login import login_required, current_user
from app.model.models import Project
from app.model.db_config import db_session
from app.forms.forms import ProjectForm
from app.utils.firebase_config import storage

projects = Blueprint('projects', __name__)


@projects.route('/projects')
@login_required
def projects_index():
    """Página de inicio de proyectos"""

    user_projects = Project.query.filter_by(
        user_email=current_user.email).all()
    project_fields = ['name', 'description', 'repository', 'user_email', 'image', 'web',]

    context = {
        'title': 'Proyectos',
        'type': 'proyecto',
        'action': url_for('projects.projects_new'),
        'delete_action': '/projects/delete/',
        'edit_action': '/projects/edit/',
        'data': user_projects,
        'fields': project_fields
    }

    return render_template('data.html', **context)


@projects.route('/projects/new', methods=['GET', 'POST'])
@login_required
def projects_new():
    """Página de creación de proyectos"""

    project_form = ProjectForm()

    context = {
        'title': 'Nuevo Proyecto',
        'form': project_form,
        'action': url_for('projects.projects_new')
    }

    if project_form.validate_on_submit():
        project_img = project_form.project_img.data if project_form.project_img.data else None
        project_img_path = None
        user_projects = Project.query.filter_by(user_email=current_user.email).all()
        project_id = 1

        if len(user_projects) > 0:
            project_id = user_projects[-1].id + 1

        if project_img:
            storage.child(f'users/{current_user.email}/project/project_{project_id}').put(project_img)
            project_img_path = storage.child(f'users/{current_user.email}/project/project_{project_id}').get_url(token=token_hex(16))

        project = Project(project_form.name.data, project_form.description.data,
                          project_form.repository.data, current_user.email, project_img_path, project_form.web.data)
        db_session.add(project)
        db_session.commit()
        
        return redirect(url_for('projects.projects_index'))

    return render_template('forms.html', **context)
