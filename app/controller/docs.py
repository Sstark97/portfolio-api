""" Controlador para manejar las habilidades de un usuario """
from flask import Blueprint, render_template, redirect, url_for, request

docs = Blueprint('docs', __name__)


@docs.route('/docs')
def docs_index():
    """ Documentación de la API """

    data = [{'title': 'Cuenta', 'routes': [{'method': 'GET', 'color': 'bg-primary',
                                            'endpoint': '/api/v1/user', 'description': 'Prueba'}, ]}]

    context = {
        'title': 'Documentación',
        'data': data
    }

    return render_template('docs.html', **context)
