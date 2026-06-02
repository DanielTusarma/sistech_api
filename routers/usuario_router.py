from fastapi import APIRouter, Depends, HTTPException, Path, Query
from typing import List     
from sqlalchemy.orm import Session
from auth.permissions import RoleChecker, ADMIN_ONLY

from database import get_db
from services.usuario_service import crear_usuario, obtener_usuario_por_id, obtener_usuario_por_email, listar_usuarios
from schemas.usuario import UsuarioCreate, UsuarioRead, UsuarioReadSencillo
from schemas.usuario import UsuarioRead

router = APIRouter(
    prefix="/api/usuarios",
    tags=["Usuarios"]
)

# ruta para crear un usuario
@router.post("/", response_model=UsuarioRead, status_code=201)
def crear_usuario_endpoint(
    datos: UsuarioCreate, 
    current_user: UsuarioRead = Depends(RoleChecker(ADMIN_ONLY)),
    db: Session = Depends(get_db)
):
    nuevo_usuario = crear_usuario(db, datos)
    return nuevo_usuario

# ruta para obtener un usuario por su id
@router.get("/{id}", response_model=UsuarioRead)
def obtener_usuario_por_id_endpoint(
    id: int = Path(..., gt=0, description="ID del usuario"), 
    current_user: UsuarioRead = Depends(RoleChecker(ADMIN_ONLY)),
    db: Session = Depends(get_db)
):
    usuario = obtener_usuario_por_id(db, id)
    
    if not usuario:
        raise HTTPException(
            status_code=404, 
            detail="Usuario no encontrado"
        )
    
    return usuario

# ruta para obtener un usuario por su email
@router.get("/email/{email}", response_model=UsuarioRead)
def obtener_usuario_por_email_endpoint(
    email: str = Path(..., description="Email del usuario"), 
    current_user: UsuarioRead = Depends(RoleChecker(ADMIN_ONLY)),
    db: Session = Depends(get_db)
):
    usuario_email = obtener_usuario_por_email(db, email)
    
    if not usuario_email:
        raise HTTPException(
            status_code=404, 
            detail="Usuario no encontrado"
        )
    
    return usuario_email


# ruta para listar todos los usuarios
@router.get("/", response_model=List[UsuarioReadSencillo])
def listar_usuarios_endpoint(
    current_user: UsuarioRead = Depends(RoleChecker(ADMIN_ONLY)),
    page: int = Query(1, ge=1, description="Número de página"),
    size: int = Query(5, ge=1, le=100, description="Tamaño de la página"),
    db: Session = Depends(get_db)
):
    usuarios = listar_usuarios(db, page=page, size=size)
    return usuarios
