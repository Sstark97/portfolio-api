""" Archivo que define el modelo de Trabajo"""
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from app.model.db_config import Base

class Work(Base):
    """Clase que define el Modelo de Trabajo"""
    __tablename__ = 'work'

    def __init__(self, position, company, description, start_date, current, user_email, final_date = None):
        self.position = position
        self.company = company
        self.description = description
        self.start_date = start_date
        self.final_date = final_date
        self.current = current
        self.user_email = user_email

    id = Column(Integer, primary_key=True, autoincrement=True)
    position = Column(String(100), nullable=False)
    company = Column(String(100), nullable=False)
    description = Column(String(500))
    start_date = Column(Date, nullable=False)
    final_date = Column(Date, CheckConstraint('final_date IS NULL OR final_date >= start_date', name='work_date_constraint'))
    current = Column(Boolean, default=False)

    user_email = Column(String(100), ForeignKey('user.email', ondelete="CASCADE"), nullable=False)
    user_work = relationship('User', back_populates='work')
