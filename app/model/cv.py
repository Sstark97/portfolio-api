""" Archivo que define el modelo de CV"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.model.db_config import Base

class Cv(Base):
    """Clase que define el Modelo de CV"""
    __tablename__ = 'cv'

    def __init__(self, presentation, user_email):
        self.presentation = presentation
        self.user_email = user_email

    id = Column(Integer, primary_key=True, autoincrement=True)
    presentation = Column(String(1000), nullable=False)
    user_email = Column(String(100), ForeignKey('user.email'), nullable=False)
    hobbies = relationship('Hobby', backref='cv', lazy=True)
    work = relationship('Work', backref='cv', lazy=True)
    education = relationship('Education', backref='cv', lazy=True)
