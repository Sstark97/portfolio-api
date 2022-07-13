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

if __name__ == '__main__':
    if environ.get('APP_LOCATION') == 'heroku':
        app.run(host="0.0.0.0", port=int(environ.get("PORT", 5000)))
    else:
        app.run(host='localhost', port=8080, debug=True)
