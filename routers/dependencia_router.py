from fastapi import APIRouter, Depends, HTTPException, Path, Query
from typing import List
from sqlalchemy.orm import Session
from auth.permissions import RoleChecker, ALL_ROLES, ADMIN_ONLY, VIEW_EMPLOYEE_ROLES

from database import get_db
from services.dependencia_service import(
    crear_dependencia,
    listar_dependencias,
    listar_empleados_dependencia,
    obtener_dependencia_por_id
)
from schemas.dependencia import DependenciaCreate, DependenciaRead
from schemas.empleado import EmpleadoReadSencillo
from schemas.usuario import UsuarioRead
from schemas.paginacion import PaginatedResponse

router = APIRouter(
    prefix="/api/dependencias",
    tags=["Dependencias"]
)

# ruta para crear una dependencia
@router.post("/", response_model=DependenciaRead, status_code=201)
def crear_dependencia_endpoint(
    datos: DependenciaCreate,
    current_user: UsuarioRead = Depends(RoleChecker(ADMIN_ONLY)),
    db: Session = Depends(get_db)
):
    # crear dependencia
    nueva_dependencia = crear_dependencia(db, datos)
    return nueva_dependencia

# ruta para listar todas las dependencias
@router.get("/", response_model=PaginatedResponse[DependenciaRead])
def listar_dependencias_endpoint(
    current_user: UsuarioRead = Depends(RoleChecker(ALL_ROLES)),
    page: int = Query(1, ge=1),
    size: int = Query(5, ge=1, le=100),    
    db: Session = Depends(get_db)):
    dependencias = listar_dependencias(db=db, page=page, size=size)
    return dependencias

# ruta para listar los empleados por dependencia
@router.get("/{id}/empleados", response_model=PaginatedResponse[EmpleadoReadSencillo])
def listar_empleados_dependencia_endpoint(
    current_user: UsuarioRead = Depends(RoleChecker(VIEW_EMPLOYEE_ROLES)),
    id: int = Path(..., gt=0, description="Id de la dependencia a consultar"),
    page: int = Query(1, ge=1),
    size: int = Query(5, ge=1, le=100),
    db: Session = Depends(get_db)
):
    dependencia = obtener_dependencia_por_id(db, id)
    
    if not dependencia:
        raise HTTPException(
            status_code=404,
            detail=f"Dependencia con Id {id} no encontrada"
        )
    
    empleados = listar_empleados_dependencia(db, id, page=page, size=size)
    return empleados
    
    



