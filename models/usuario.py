from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime, UTC
from database import Base

class Usuario(Base):
    # nombre de la tabla usuarios en la BD
    __tablename__ = "usuarios"
    
    # Id y llave primaria
    id = Column(Integer, primary_key=True, index=True)
    
    # nombre de usuario
    nombre = Column(String, nullable=False)
    
    # email de usuario
    email = Column(String, unique=True, nullable=False)
    
    # password de usuario
    password = Column(String, nullable=False)
    
    # rol de usuario
    rol = Column(String, nullable=False)
    
    # activo (si/no True/False)
    activo = Column(Boolean, default=True, nullable=False)
    
    # fecha de creacion de usuario
    fecha_creacion = Column(DateTime, default=lambda: datetime.now(UTC))
    