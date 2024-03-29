""" Archivo que define el modelo de Proyectos"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.model.db_config import Base

class Project(Base):
    """Clase que define el Modelo de Proyectos"""
    __tablename__ = 'project'

    def __init__(self, name, description, repository, user_email, image=None, web=None):
        self.name = name
        self.description = description
        self.image = image
        self.web = web
        self.repository = repository
        self.user_email = user_email
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(1000), nullable=False)
    image = Column(String(500))
    web = Column(String(300))
    repository = Column(String(300), nullable=False)

    user_email = Column(String(100), ForeignKey('user.email', ondelete="CASCADE"), nullable=False)
    user_project = relationship('User', back_populates='project')
