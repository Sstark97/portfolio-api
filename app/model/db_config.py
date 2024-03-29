""" Archivo de configuración de la Base de Datos"""
from os import getenv
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()
DATA_BASE_URI = getenv('DATABASE_URL' )
if DATA_BASE_URI and DATA_BASE_URI.startswith("postgres://"):
    DATA_BASE_URI = DATA_BASE_URI.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATA_BASE_URI)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    """Inicializa la Base de Datos"""
    import app.model.user
    import app.model.project
    import app.model.work
    import app.model.education
    import app.model.hobby
    import app.model.skill

    Base.metadata.create_all(bind=engine, checkfirst=True)
