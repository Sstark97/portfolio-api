"""Archivo que define el Modelo de Usuarios"""
import re
from flask_login import UserMixin
from sqlalchemy import Column, String, LargeBinary
from sqlalchemy.orm import relationship, validates
from app.model.db_config import Base
class User(UserMixin, Base):
    """Clase que define el Modelo de Usuarios"""
    __tablename__ = 'user'

    def __init__(self, email, name, surname, adress, phone, password, api_token, presentation=None, avatar=None):
        self.email = email
        self.name = name
        self.surname = surname
        self.adress = adress
        self.phone = phone
        self.password = password
        self.presentation = presentation
        self.avatar = avatar
        self.api_token = api_token

    email = Column(String(100), primary_key=True)
    name = Column(String(100), nullable=False)
    surname = Column(String(100))
    presentation = Column(String(1000))
    adress = Column(String(100))
    phone = Column(String(100))
    password = Column(LargeBinary(400), nullable=False)
    avatar = Column(String(500))
    api_token = Column(String(150))
    hobbies = relationship('Hobby', back_populates='user_hobby', cascade='all, delete, delete-orphan')
    skills = relationship('Skill', back_populates='user_skill', cascade='all, delete, delete-orphan')
    work = relationship('Work', back_populates='user_work', cascade='all, delete, delete-orphan')
    education = relationship('Education', back_populates='user_education', cascade='all, delete, delete-orphan')
    project = relationship('Project', back_populates='user_project', cascade='all, delete, delete-orphan')

    def get_id(self):
        return self.email

    @validates('email')
    def validate_email(self, key, adress):
        """Valida el formato de email"""
        # pylint: disable=unused-argument

        patt = re.compile(r"[\w]{4,20}@[\w]{4,12}.com")
        if not re.fullmatch(patt,adress):
            raise ValueError(f'{adress} is not an email')
        return adress
    
    @validates('phone')
    def validate_phone(self, key, new_phone):
        """Valida el formato del telefono"""
        # pylint: disable=unused-argument

        patt = re.compile(r"[\d]{9}")
        if not re.fullmatch(patt,new_phone):
            raise ValueError(f'{new_phone} is not a phone')
        return new_phone
