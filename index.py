""" Archivo inicial de la App de Flask"""
import unittest
from datetime import date
from flask import render_template, jsonify,make_response
from app import create_app
from app.config import Config
from app.model.db_config import init_db, db_session
from app.model.user import User
from app.model.proyect import Proyect
from app.model.cv import Cv
from app.model.work import Work
from app.model.education import Education
from app.model.hobby import Hobby

app = create_app()
app.config.from_object(Config())
init_db()

@app.cli.command()
def test():
    """Ejecuta los tests"""
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    unittest.TextTestRunner(verbosity=2).run(tests)

@app.route('/')
def index():
    """Página de Inicio"""
    user = User("aitor@gmail.com", "Aitor", "Gonzalez", "San", "633666666", "12345567", "sqwrqr")
    db_session.add(user)
    db_session.commit()

    proyect = Proyect("Proyecto 1", "Descripción del proyecto 1", "https://www.google.com", "web", "repo", "aitor@gmail.com")
    db_session.add(proyect)
    db_session.commit()

    cv = Cv("CV de Aitor", "aitor@gmail.com")
    db_session.add(cv)
    db_session.commit()

    work = Work("Cargo 1", "Empresa 1",  date(2020, 5, 17), False, 1)
    db_session.add(work)
    db_session.commit()

    education = Education("Estudios 1", "Institución 1", date(2020, 5, 17), False, 1, 1)
    db_session.add(education)
    db_session.commit()

    hobby = Hobby("Hobby 1", 1)
    db_session.add(hobby)
    db_session.commit()

    return render_template('index.html')

@app.route('/test')
def testing():
    """Página de Test"""

    user_data = db_session.query(User.email, User.name, Proyect.name).join(Proyect).filter(User.email == Proyect.user_email).one()

    data_1 = {
        'email': user_data[0],
        'name': user_data[1],
        'proyect': user_data[2]
    }

    return make_response(jsonify(message="Okey",data = data_1), 200)

if __name__ == '__main__':
    app.run(port = 3000, debug = True)
