from pydantic import BaseModel, Field, field_validator, EmailStr
from typing import Optional
from decimal import Decimal
from datetime import date
from .dependencia import DependenciaRead, DependenciaReadSencilla
from .cargo import CargoRead

class EmpleadoBase(BaseModel):
    nombres: str = Field(..., min_length=2, max_length=50, description="nombres del empleado")
    apellidos: str = Field(..., min_length=2, max_length=50, description="apellidos del empleado")
    telefono: str = Field(..., min_length=7, max_length=15, pattern=r'^\+?\d+$', description="telefono del empleado")
    email: EmailStr =Field(max_length=254, description="email del empleado")
    salario: Decimal = Field(max_digits=10, decimal_places=2, gt=0, description="salario del empleado")
    fecha_ingreso: date
    
    # validacion adicional
    @field_validator("nombres", "apellidos")
    def no_vacios(cls, valor):
        if not valor.strip():
            raise ValueError("El campo no puede estar vacío o contener solo espacios")
        return valor
    
class EmpleadoCreate(EmpleadoBase):
    dependencia_id: int = Field(..., gt=0, description="id de la dependencia a la que pertenece el empleado")
    
    
class EmpleadoUpdate(BaseModel):
    
    nombres: Optional[str] = Field(None, min_length=2, max_length=50)
    apellidos: Optional[str] = Field(None, min_length=2, max_length=50)
    telefono: Optional[str] = Field(None, min_length=7, max_length=15, pattern=r'^\+?\d+$')
    email: Optional[EmailStr] = Field(None, max_length=254)
    salario: Optional[Decimal] = Field(None, max_digits=10, decimal_places=2, gt=0)
    fecha_ingreso: Optional[date] = None
    dependencia_id: Optional[int] = Field(None, gt=0)
    cargo_id: Optional[int] = Field(None, gt=0)
    
    # validacion adicional
    @field_validator("nombres", "apellidos")
    def no_vacios(cls, valor):
        if valor is not None and not valor.strip():
            raise ValueError("El campo no puede estar vacío o contener solo espacios")
        return valor
    
class EmpleadoDesactivar(BaseModel):
    fecha_salida: date = Field(..., description="fecha de salida del empleado")
    
class EmpleadoRead(EmpleadoBase):
    id: int
    activo: bool
    dependencia: DependenciaRead
    cargo: Optional[CargoRead] = None
    fecha_salida: Optional[date] = None
    
    model_config = {
        "from_attributes": True
    }
    
class EmpleadoReadSencillo(BaseModel):
    id: int
    nombres: str
    apellidos: str
    dependencia: DependenciaReadSencilla
    
    
    
    
    
    
    
    
