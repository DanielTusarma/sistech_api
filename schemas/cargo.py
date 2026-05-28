from pydantic import BaseModel, Field, field_validator
from typing import Optional

class CargoBase(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=30, description="nombre del cargo")
    descripcion: str = Field(..., min_length=2, max_length=255, description="descripción del cargo")
    
    # validacion
    @field_validator("nombre")
    def no_vacios(cls, valor):
        if not valor.strip():
            raise ValueError("El campo de nombre no puede estar vacío")
        return valor
    
class CargoCreate(CargoBase):
    pass

class CargoRead(BaseModel):
    
    id: int
    nombre: str
    descripcion: str
    
    model_config = {
        "from_attributes": True
    }
    
