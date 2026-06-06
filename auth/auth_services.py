# Archivo que contiene la lógica de autenticación de usuarios.
# Aquí se valida si el usuario existe y si la contraseña es correcta.
# También se coordina la generación del token JWT después del login.

from sqlalchemy.orm import Session
from repositories.usuario_repository import UsuarioRepository
from .security import verify_password, create_access_token

# Función para autenticar al usuario
def authenticate_user(db: Session, email: str, password: str):
    repository = UsuarioRepository(db)
    usuario = repository.get_usuario_email(email)
    
    if not usuario:
        raise ValueError("Usuario no encontrado")
    if not verify_password(password, usuario.password):
        raise ValueError("Contraseña incorrecta")
    return usuario

# Función para manejar el proceso de login y generación de token JWT      
def login_user(db: Session, email: str, password: str):
    usuario = authenticate_user(db, email, password)
    access_token = create_access_token(
        data={
            "sub": str(usuario.id),
            "rol": usuario.rol
        }
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "usuario": {
            "id": usuario.id,
            "email": usuario.email,
            "rol": usuario.rol
        }
    }

