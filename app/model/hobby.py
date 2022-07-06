""" Archivo que define el modelo de Hobbies"""
from sqlalchemy import Column, Integer, String, ForeignKey
from app.model.db_config import Base

class Hobby(Base):
    """Clase que define el Modelo de Hobbies"""
    __tablename__ = 'hobby'

    def __init__(self, name, user_email):
        self.name = name
        self.user_email = user_email

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    user_email = Column(String(100), ForeignKey('user.email'), nullable=False)
