""" Archivo inicial de la App de Flask"""
from atexit import register
import unittest
from flask import render_template
from flask_login import current_user, login_required
from app import create_app
from app.controller.auth import auth
from app.config import Config
from app.model.db_config import init_db
from app.forms.register_form import RegisterForm

app = create_app()
app.config.from_object(Config())
init_db()

app.register_blueprint(auth)


@app.cli.command()
def test():
    """Ejecuta los tests"""
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    unittest.TextTestRunner(verbosity=2).run(tests)


@app.route('/')
def index():
    """Página de Inicio"""

    return render_template('index.html')

@app.route('/about')
def about():
    """Página de Acerca de"""
    form = RegisterForm()

    return render_template('account.html', form=form)


@app.route('/home')
@login_required
def home():
    """Página Principal"""

    return render_template('home.html')

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
    app.run(port=3000, debug=True)
