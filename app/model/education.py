""" Archivo que define el modelo de Eduación"""
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, CheckConstraint
from app.model.db_config import Base

class Education(Base):
    """Clase que define el Modelo de Eduación"""
    __tablename__ = 'education'

    def __init__(self, study, education_institution, description, start_date, current, course, user_email, final_date=None):
        self.study = study
        self.education_institution = education_institution
        self.description = description
        self.start_date = start_date
        self.final_date = final_date
        self.current = current
        self.course = course
        self.user_email = user_email

    id = Column(Integer, primary_key=True, autoincrement=True)
    study = Column(String(100), nullable=False)
    education_institution = Column(String(100), nullable=False)
    description = Column(String(500))
    start_date = Column(Date, nullable=False)
    final_date = Column(Date, CheckConstraint('final_date IS NULL OR final_date >= start_date', name='work_date_constraint'))
    current = Column(Boolean, default=False)
    course = Column(Integer)
    user_email = Column(String(100), ForeignKey('user.email'), nullable=False)
    