from fastapi import APIRouter, Depends, HTTPException, Path, Query
from typing import List
from sqlalchemy.orm import Session
from auth.permissions import RoleChecker, ADMIN_ONLY, ALL_ROLES, VIEW_EMPLOYEE_ROLES, MANAGEMENT_ROLES

from database import get_db
from services.cargo_service import(
    crear_cargo,
    listar_cargos,
    listar_empleados_cargo,
    obtener_cargo_por_id
)
from schemas.cargo import CargoCreate, CargoRead
from schemas.empleado import EmpleadoReadSencillo
from schemas.usuario import UsuarioRead
from schemas.paginacion import PaginatedResponse

router = APIRouter(
    prefix="/api/cargos",
    tags=["Cargos"]
)

# ruta para crear un cargo
@router.post("/", response_model=CargoRead, status_code=201)
def crear_cargo_endpoint(
    datos: CargoCreate,
    current_user: UsuarioRead = Depends(RoleChecker(ADMIN_ONLY)),
    db: Session = Depends(get_db)
):
    # crear cargo
    nuevo_cargo = crear_cargo(db, datos)
    return nuevo_cargo

# ruta para listar todos los cargos
@router.get("/", response_model=PaginatedResponse[CargoRead])
def listar_cargos_endpoint(
    current_user: UsuarioRead = Depends(RoleChecker(ALL_ROLES)),
    page: int = Query(1, ge=1),
    size: int = Query(5, ge=1, le=100),
    db: Session = Depends(get_db)
):
    cargos = listar_cargos(db=db, page=page, size=size)
    return cargos

# ruta para listar los empleados por cargo
@router.get("/{id}/empleados", response_model=PaginatedResponse[EmpleadoReadSencillo])
def listar_empleados_cargo_endpoint(
    id: int = Path(..., gt=0, description="Id del cargo a consultar"),
    current_user: UsuarioRead = Depends(RoleChecker(VIEW_EMPLOYEE_ROLES)),
    page: int = Query(1, ge=1),
    size: int = Query(5, ge=1, le=100),    
    db: Session = Depends(get_db)
):
    cargo = obtener_cargo_por_id(db, id)
    
    if not cargo:
        raise HTTPException(
            status_code=404,
            detail=f"Cargo con Id {id} no encontrado"
        )
        
    empleados = listar_empleados_cargo(db, id, page=page, size=size)
    return empleados
