# Archivo que contiene dependencias reutilizables de autenticación.
# Aquí se obtiene el usuario autenticado a partir del token JWT.
# Estas dependencias se utilizan para proteger endpoints del sistema.

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session

from .security import verify_access_token
from database import get_db
from repositories.usuario_repository import UsuarioRepository

# obtener el usuario actual a partir del token JWT
def get_current_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl="/api/auth/login")),
    db: Session = Depends(get_db)
):
    payload = verify_access_token(token)
    user_id = payload.get("sub")
    
    repository = UsuarioRepository(db)
    
    usuario = repository.get_usuario(user_id)
    if not usuario:
        raise JWTError("Usuario no encontrado")
    return usuario