""" Controlador para manejar las habilidades de un usuario """
from flask import Blueprint, render_template, redirect, url_for, request

docs = Blueprint('docs', __name__)


@docs.route('/docs')
def docs_index():
    """ Documentación de la API """

    data = [
        {
            'routes': [
                {
                    'method': 'GET', 
                    'color': 'bg-primary',
                    'endpoint': '/api/v1/user', 
                    'description': 'Obtiene los datos de la Cuenta'
                },
                {
                    'method': 'GET', 
                    'color': 'bg-primary',
                    'endpoint': '/api/v1/user/all', 
                    'description': 'Obtiene todos los datos de la cuenta, todo el PortFolio'  
                }
            ],
        },
        {
            'routes': [
                {
                    'method': 'GET', 
                    'color': 'bg-primary',
                    'endpoint': '/api/v1/projects', 
                    'description': 'Obtiene todos los proyectos de una Cuenta'
                }
            ]
        },
        {
            'routes': [
                {
                    'method': 'GET', 
                    'color': 'bg-primary',
                    'endpoint': '/api/v1/education', 
                    'description': 'Obtiene todos los Datos Académicos de una Cuenta'
                }
            ]
        },
        {
            'routes': [
                {
                    'method': 'GET', 
                    'color': 'bg-primary',
                    'endpoint': '/api/v1/work', 
                    'description': 'Obtiene todos la Experiencia Laboral de una Cuenta'
                }
            ]
        },
        { 
            'routes': [
                {
                    'method': 'GET', 
                    'color': 'bg-primary',
                    'endpoint': '/api/v1/skills', 
                    'description': 'Obtiene todos las Habilidades de una Cuenta'
                }
            ]
        },
        {
            'routes': [
                {
                    'method': 'GET', 
                    'color': 'bg-primary',
                    'endpoint': '/api/v1/hobbies', 
                    'description': 'Obtiene todos los Hobbies de una Cuenta'
                }
            ]
        },
    ]

    context = {
        'title': 'Documentación',
        'data': data
    }

    return render_template('docs.html', **context)
