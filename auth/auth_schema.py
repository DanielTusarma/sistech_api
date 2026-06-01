# Archivo que contiene schemas relacionados con autenticación.
# Aquí se definen modelos de entrada y salida para login y tokens JWT.
# Sirve para validar datos y documentar automáticamente la API.

from pydantic import BaseModel, Field, field_validator

class LoginRequest(BaseModel):
    email: str = Field(..., max_length=254, description="email del usuario")
    password: str = Field(..., min_length=8, max_length=64, description="password del usuario")
    
    # validacion adicional
    @field_validator("email")
    def email_no_vacio(cls, valor):
        if not valor.strip():
            raise ValueError("El campo de email no puede estar vacío o contener solo espacios")
        return valor
    
