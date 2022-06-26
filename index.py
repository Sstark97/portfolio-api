from flask import render_template
import unittest
from app import create_app
app = create_app()

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    unittest.TextTestRunner(verbosity=2).run(tests)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port = 3000, debug = True)