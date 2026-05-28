from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Numeric, Date
from database import Base
from sqlalchemy.orm import relationship

class Empleado(Base):
    # nombre de la tabla empleados en la base de datos sistech_db
    __tablename__ = "empleados"
    
    # Id autoincremental y llave primaria
    id = Column(Integer, primary_key=True, index=True)
    
    # nombres del empleado
    nombres = Column(String, nullable=False)
    
    # apellidos del empleado
    apellidos = Column(String, nullable=False)
    
    # telefono del empleado
    telefono = Column(String, nullable=False)
    
    # email del empleado
    email = Column(String, unique=True, nullable=False)
    
    # salario del empleado
    salario = Column(Numeric(10,2), nullable=False)
    
    # fecha ingreso del empleado
    fecha_ingreso = Column(Date, nullable=False)
    
    # fecha salida del empleado
    fecha_salida = Column(Date, nullable=True)
    
    # instancia de actividad de un empleado en la empresa
    activo = Column(Boolean, default=True, nullable=False)
    
    # clave foranea dependencia
    dependencia_id = Column(Integer, ForeignKey("dependencias.id"), nullable=False)
    
    # clave foranea cargo
    cargo_id = Column(Integer, ForeignKey("cargos.id"), nullable=True)
    
    # Relacion dependencia
    dependencia = relationship("Dependencia", back_populates="empleados")
    
    # Relacion cargo
    cargo = relationship("Cargo", back_populates="empleados")
    
    
    
