"""Archivo que define el Modelo de Usuarios"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.model.db_config import Base

class User(Base):
    """Clase que define el Modelo de Usuarios"""
    __tablename__ = 'user'
    def __init__(self, email, name, surname, adress, phone, password, api_token):
        self.email = email
        self.name = name
        self.surname = surname
        self.adress = adress
        self.phone = phone
        self.password = password
        self.api_token = api_token

    email = Column(String(100), primary_key=True)
    name = Column(String(100), nullable=False)
    surname = Column(String(100))
    adress = Column(String(100))
    phone = Column(String(100))
    password = Column(String(100), nullable=False)
    api_token = Column(String(100))
    cv = relationship('Cv', backref='user', lazy=True)
    proyect = relationship('Proyect', backref='user', lazy=True)
