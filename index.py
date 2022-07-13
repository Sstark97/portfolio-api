""" Archivo inicial de la App de Flask"""
from os import environ
import unittest
from flask import render_template
from app import create_app
from app.config import Config

app = create_app()
app.config.from_object(Config())

@app.cli.command()
def test():
    """Ejecuta los tests"""
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    unittest.TextTestRunner(verbosity=2).run(tests)


@app.route('/')
def index():
    """Página de Inicio"""

    return render_template('home.html', title='Bienvenido')

# @app.route('/test')
# def testing():
#     """Página de Test"""

#     user_data = db_session.query(User).filter(User.email == "aitorscinfo@gmail.com").one()

#     data_1 = {
#         'email': user_data.email,
#         'name': user_data.name,
#         'surname': user_data.surname,
#         'adress': user_data.adress,
#         'phone': user_data.phone,
#         'avatar': user_data.avatar,
#         'token': user_data.api_token
#     }

#     return make_response(jsonify(message="Okey",data = data_1), 200)


if __name__ == '__main__':
    """ Ejecuta la App """
    app.run()
