from pydantic import BaseModel, Field, field_validator, EmailStr
from typing import Optional
from datetime import datetime
from models.enum import RolUsuario

class UsuarioBase(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=100, description="nombre des usuario")
    email: EmailStr = Field(max_length=254, description="email del usuario")
    password: str = Field(min_length=8, max_length=64, description="password del usuario")
    rol: RolUsuario = Field(description="rol del usuario")

    # validacion adicional
    @field_validator("nombre")
    def no_vacios(cls, valor):
        if not valor.strip():
            raise ValueError("El campo no puede estar vacío o contener solo espacios")
        return valor
    
class UsuarioCreate(UsuarioBase):
    pass   

class UsuarioRead(BaseModel):
    id: int
    nombre: str
    email: EmailStr
    rol: RolUsuario
    activo: bool
    fecha_creacion: datetime
    
    model_config = {
        "from_attributes": True
    }
    
class UsuarioReadSencillo(BaseModel):
    nombre: str
    email: EmailStr
    rol: RolUsuario
    
    model_config = {
        "from_attributes": True
    }