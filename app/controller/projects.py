""" Controlador que se encarga de la autenticación de los proyectos de un usuario """
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.model.models import Proyect, User
from app.utils.firebase_config import storage

projects = Blueprint('projects', __name__)

@projects.route('/projects')
@login_required
def projects_index():
    """Página de inicio de proyectos"""

    user_projects = Proyect.query.filter_by(user_email=current_user.email).all()

    print(user_projects)

    context = {
        'type': 'proyecto',
        'action': '',
        'data': user_projects
    }

    return render_template('data.html', **context)
