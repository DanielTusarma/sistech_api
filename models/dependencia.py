from sqlalchemy import Column, String, Integer, Boolean
from database import Base
from sqlalchemy.orm import relationship

class Dependencia(Base):
    # nombre de la tabla en la base de datos sistech_db
    __tablename__ = "dependencias"
    
    # Id autoincremental y llave primaria
    id = Column(Integer, primary_key=True, index=True)
    
    # nombre de la dependencia
    nombre = Column(String, nullable=False)
    
    # instancia de actividad de una dependencia en la empresa
    activo = Column(Boolean, default=True, nullable=False)
    
    # relacion
    empleados = relationship("Empleado", back_populates="dependencia")
    