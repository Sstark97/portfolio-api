""" Archivo que define el modelo de Hobbies"""
from sqlalchemy import Column, Integer, String, ForeignKey
from app.model.db_config import Base

class Hobby(Base):
    """Clase que define el Modelo de Hobbies"""
    __tablename__ = 'hobby'

    def __init__(self, name, cv_id):
        self.name = name
        self.cv_id = cv_id

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    cv_id = Column(Integer, ForeignKey('cv.id'), nullable=False)
