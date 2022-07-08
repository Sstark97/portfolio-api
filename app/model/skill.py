""" Archivo que define el modelo de Habilidades"""
from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint
from app.model.db_config import Base

class Skill(Base):
    """Clase que define el Modelo de Habilidades"""
    __tablename__ = 'skill'

    def __init__(self, name, level, user_email):
        self.name = name
        self.level = level
        self.user_email = user_email

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    level = Column(Integer, CheckConstraint('level > 0 AND level <= 10'), nullable=False)
    user_email = Column(String(100), ForeignKey('user.email'), nullable=False)
