""" Constantes de la App """

education_fields = ['study', 'education_institution', 'description', 'start_date', 'final_date', 'current', 'course']

hobby_fields = ['name']

project_fields = ['name', 'description', 'repository', 'user_email', 'image', 'web']

skills_fields = ['name', 'level']

work_fields = ['position', 'company', 'description', 'start_date', 'final_date', 'current']

docs_data = [
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
