""" Archivo que define el modelo de Trabajo"""
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, CheckConstraint
from app.model.db_config import Base

class Work(Base):
    """Clase que define el Modelo de Trabajo"""
    __tablename__ = 'work'

    def __init__(self, position, company, start_date, current, cv_id, final_date = None):
        self.position = position
        self.company = company
        self.start_date = start_date
        self.final_date = final_date
        self.current = current
        self.cv_id = cv_id

    id = Column(Integer, primary_key=True, autoincrement=True)
    position = Column(String(100), nullable=False)
    company = Column(String(100), nullable=False)
    start_date = Column(Date, nullable=False)
    final_date = Column(Date, CheckConstraint('final_date IS NULL OR final_date >= start_date', name='work_date_constraint'))
    current = Column(Boolean, default=False)

    cv_id = Column(Integer, ForeignKey('cv.id'), nullable=False)
