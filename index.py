""" Archivo inicial de la App de Flask"""
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
    app.run()
