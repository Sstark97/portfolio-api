""" Controlador que se encarga de la autenticación de los proyectos de un usuario """
from secrets import token_hex
from flask import Blueprint, redirect, render_template, url_for, request
from flask_login import login_required, current_user
from app.model.models import Project
from app.model.db_config import db_session
from app.forms.forms import ProjectForm, DeleteDataForm
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
        'message': 'No hay proyectos, añada uno nuevo',
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

@projects.route('/projects/edit/<int:project_id>', methods=['GET', 'POST'])
@login_required
def projects_edit(project_id):
    """ Página para editar un Proyecto """

    project = Project.query.filter_by(id=project_id).first()

    project_form = ProjectForm(request.form) if request.method == 'POST' else ProjectForm(obj=project)
    project_form.submit.label.text = 'Editar'
    

    context = {
        'title': 'Editar Proyecto',
        'form': project_form,
        'action': url_for('projects.projects_edit', project_id=project_id)
    }

    if project_form.validate_on_submit() and request.method == 'POST':
        project_path = None
        project_img = request.files.get('project_img') if request.files.get('project_img') else None

        if project_img:
            storage.delete(f'users/{current_user.email}/project/project_{project_id}', token=token_hex(16))
            storage.child(f'users/{current_user.email}/project/project_{project_id}').put(project_img)
            project_path = storage.child(f'users/{current_user.email}/project/project_{project_id}').get_url(token=token_hex(16))
        
        project.name = project_form.name.data
        project.description = project_form.description.data
        project.repository = project_form.repository.data
        project.web = project_form.web.data
        project.image = project_path if project_path else project.image
        db_session.commit()

        return redirect(url_for('projects.projects_index'))

    return render_template('forms.html', **context)

@projects.route('/projects/delete/<int:project_id>', methods=['GET', 'POST'])
@login_required
def projects_delete(project_id):
    """ Página para eliminar un Proyecto """

    project = Project.query.filter_by(id=project_id).first()
    delete_form = DeleteDataForm()

    context = {
        'title': 'Eliminar Proyecto',
        'type': 'proyecto',
        'name': project.name,
        'delete': True,
        'form': delete_form,
        'action': url_for('projects.projects_delete', project_id=project_id),
    }
    
    if delete_form.validate_on_submit():
        if project.image:
            storage.delete(f'users/{current_user.email}/project/project_{project_id}', token=token_hex(16))

        db_session.delete(project)
        db_session.commit()

        return redirect(url_for('projects.projects_index'))

    return render_template('forms.html', **context)
