""" Archivo de configuración de la Base de Datos"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///portfolio.db?check_same_thread=False')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    """Inicializa la Base de Datos"""
    import app.model.user
    import app.model.project
    import app.model.cv
    import app.model.work
    import app.model.education
    import app.model.hobby

    Base.metadata.create_all(bind=engine)
