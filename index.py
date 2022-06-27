""" Archivo inicial de la App de Flask"""
import unittest
from flask import render_template
from app import create_app
from app.controller.auth import auth
from app.config import Config
from app.model.db_config import init_db

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

# @app.route('/test')
# def testing():
#     """Página de Test"""

#     user_data = db_session.query(User.email, User.name, Proyect.name).join(Proyect).filter(User.email == Proyect.user_email).one()
#     user = User("pepe@pepe.com", "Aitor", "Gonzalez", "San", "12344", "12345567", "sqwrqr")
#     db_session.add(user)
#     db_session.commit()

#     data_1 = {
#         'email': user_data[0],
#         'name': user_data[1],
#         'proyect': user_data[2]
#     }

#     return make_response(jsonify(message="Okey",data = data_1), 200)

if __name__ == '__main__':
    app.run(port = 3000, debug = True)
