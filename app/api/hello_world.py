""" Ruta de Prueba de la API """
from flask_restful import Resource

class HelloWorld(Resource):
    """ Clase de Prueba de la API """

    def get(self):
        """ Método de Prueba de la API """
        return {'hello': 'world'}