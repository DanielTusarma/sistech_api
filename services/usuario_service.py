from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from schemas.usuario import UsuarioRead, UsuarioCreate
from repositories.usuario_repository import UsuarioRepository
from auth.security import hash_password

# servicio para crear un usuario
def crear_usuario(db: Session, datos: UsuarioCreate):
    repository = UsuarioRepository(db)
    
    usuario_existente = repository.get_usuario_email(datos.email)

    
    if usuario_existente:
        raise ValueError("El email ya se encuentra registrado")
    
    # hashear password
    password_hasheada = hash_password(datos.password)
    
    # crear un nuevo diccionario con datos del usuario, pero con el password hasheado
    datos_usuario = {
        "nombre": datos.nombre,
        "email": datos.email,   
        "password": password_hasheada,
        "rol": datos.rol  
    }
    
    try:
                
        nuevo_usuario = repository.create_usuario(datos_usuario)
        
        db.commit()
        db.refresh(nuevo_usuario)
        
        return nuevo_usuario
    
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    
# servicio para obtener un usuario por su id
def obtener_usuario_por_id(db: Session, id: int):
    repository = UsuarioRepository(db)
    
    usuario = repository.get_usuario(id)
    
    return usuario

# servicio para obtener un usuario por su email
def obtener_usuario_por_email(db: Session, email: str):
    repository = UsuarioRepository(db)
    usuario_email = repository.get_usuario_email(email)

    return usuario_email  

# servicio para listar todos los usuarios
def listar_usuarios(db: Session, page: int = 1, size: int = 5):
    repository = UsuarioRepository(db)
    skip = (page - 1) * size
    usuarios = repository.get_usuarios_all(skip=skip, limit=size)
    return usuarios