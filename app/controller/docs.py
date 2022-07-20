""" Controlador para manejar las habilidades de un usuario """
from flask import Blueprint, render_template
from app.utils.const import docs_data

docs = Blueprint('docs', __name__)


@docs.route('/docs')
def docs_index():
    """ Documentación de la API """

    context = {
        'title': 'Documentación',
        'data': docs_data
    }

    return render_template('docs.html', **context)
