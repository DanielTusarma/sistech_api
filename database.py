# configuracion de la base de datos e importaciones
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

# cargar las variables de entorno
load_dotenv()

# construccion de la base de datos
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# creacion del motor de conexion
engine = create_engine(DATABASE_URL, echo=True)

# creacion de un SessionLocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# clase Base para los models
Base = declarative_base()

# dependencia para fastapi, obtiene una sesion a la BD por peticion
def det_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
