""" Ruta para enviar un Formulario de Contacto """
from flask import request, jsonify
from flask_restful import Resource, reqparse
from app.model.db_config import db_session
from app.model.models import User
from app.utils.decorators import token_required
from app.utils.contact_email import send_contact_email

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help='Name is required')
parser.add_argument('email', type=str, required=True, help='Email is required')
parser.add_argument('subject', type=str, required=True, help='Subject is required')
parser.add_argument('message', type=str, required=True, help='Message is required')

class ContactEmail(Resource):
    """ Recurso para los Datos Académicos de un Usuario """

    @token_required
    def post(self):
        """ Método que envía un Correo de Contacto """

        request.get_json(force=True)
        args = parser.parse_args()

        token = request.headers['x-access-tokens']
        user_email = db_session.query(User.email).filter(User.api_token == token).first()[0]

        args_keys = list(args.keys())

        if "name" in args_keys and "email" in args_keys and "subject" in args_keys and "message" in args_keys:
            send_contact_email(args, user_email)
            return jsonify({'message': 'Email sent'})
