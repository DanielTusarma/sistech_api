from pydantic import BaseModel, Field, field_validator
from typing import Optional

class DependenciaBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=30, description="nombre de la dependencia")
    
    # validacion
    @field_validator("nombre")
    def no_vacios(cls, valor):
        if not valor.strip():
            raise ValueError("El campo de nombre no puede estar vacío")
        return valor
    
class DependenciaCreate(DependenciaBase):
    pass

class DependenciaRead(BaseModel):
    
    id: int
    nombre: str
    activo: bool
    
    model_config = {
        "from_attributes": True
    }
    
class DependenciaReadSencilla(BaseModel):
    nombre: str
    
    