""" Archivo de configuración de la Base de Datos"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///portfolio.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    """import all modules here that might define models so that"""
    import app.model.user
    import app.model.proyect
    import app.model.cv
    import app.model.work
    import app.model.education
    import app.model.hobby

    Base.metadata.create_all(bind=engine)
