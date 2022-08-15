""" Archivo para el manejo de correos electrónicos. """
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
from os import getenv
from dotenv import load_dotenv

load_dotenv()


def send_contact_email(contact_form, destinator):
    """ Envía un correo electrónico de cambio de contraseña. """
    smtp_address = 'smtp.gmail.com'
    smtp_port = 465

    email_address = getenv('EMAIL')
    email_password = getenv('EMAIL_PASSWORD')

    # Creación del mensaje
    message = MIMEMultipart("alternative")
    # Añadir un asunto
    message["Subject"] = contact_form.subject
    # Añadir un emisor
    message["From"] = "PortFolio API"
    # Añadir un destinatario
    message["To"] = destinator

    texte = f'''
    {contact_form.name} ha enviado un mensaje a través de la API de PortFolio.
    El Correo de Contacto es: {contact_form.email}
    El Mensaje es el siguiente:
    {contact_form.message}
            '''

    texte_mime = MIMEText(texte, 'plain')

    message.attach(texte_mime)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
        # Conexion al servidor
        server.login(email_address, email_password)
        # Envio del correo
        server.sendmail(email_address, destinator, message.as_string())
