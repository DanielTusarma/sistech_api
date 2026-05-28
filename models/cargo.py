from sqlalchemy import Column, Integer, String, Boolean
from database import Base
from sqlalchemy.orm import relationship

class Cargo(Base):
    # nombre de la nueva tabla en la BD
    __tablename__ = "cargos"
    
    # Id
    id = Column(Integer, primary_key=True, index=True)
    
    # nombre del cargo
    nombre = Column(String, nullable=False)
    
    # descripcion
    descripcion = Column(String, nullable=False)
    
    # instancia de actividad del cargo
    activo = Column(Boolean, default=True, nullable=False)
    
    # relacion con entidad empleados
    empleados = relationship("Empleado", back_populates="cargo")
    
    