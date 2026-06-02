from fastapi import APIRouter, Depends, HTTPException, Path, Query
from typing import List
from sqlalchemy.orm import Session
from auth.permissions import RoleChecker, ALL_ROLES, VIEW_EMPLOYEE_ROLES, MANAGEMENT_ROLES, ADMIN_ONLY

from database import get_db
from services.empleado_service import(
    crear_empleado,
    listar_empleados_detalle,
    obtener_empleado_por_id,
    editar_empleado, 
    desactivar_empleado,
    listar_empleados_activos, 
    listar_empleados_inactivos
)
from schemas.empleado import EmpleadoCreate, EmpleadoRead, EmpleadoUpdate, EmpleadoDesactivar, EmpleadoReadSencillo
from schemas.usuario import UsuarioRead

router = APIRouter(
    prefix="/api/empleados",
    tags=["Empleados"]
)

# ruta para crear un empleado
@router.post("/", response_model=EmpleadoRead, status_code=201)
def crear_empleado_endpoint(
    datos: EmpleadoCreate, 
    current_user: UsuarioRead = Depends(RoleChecker(ADMIN_ONLY)),
    db: Session = Depends(get_db)
):
    # crear un empleado
    nuevo_empleado = crear_empleado(db, datos)
    return nuevo_empleado


# ruta para listar todos los empleados con todos sus detalles
@router.get("/", response_model=List[EmpleadoRead])
def obtener_empleados_detalle_endpoint(
    current_user: UsuarioRead = Depends(RoleChecker(VIEW_EMPLOYEE_ROLES)),
    page: int = Query(1, ge=1),
    size: int = Query(5, ge=1, le=100),    
    db: Session = Depends(get_db)
):
    empleados = listar_empleados_detalle(db=db, page=page, size=size)
    return empleados

# ruta para listar todos los empleados con detalles resumidos
@router.get("/resumen", response_model=List[EmpleadoReadSencillo])
def obtener_empleados_resumido_endpoint(
    current_user: UsuarioRead = Depends(RoleChecker(VIEW_EMPLOYEE_ROLES)),
    page: int = Query(1, ge=1),
    size: int = Query(5, ge=1, le=100),     
    db: Session = Depends(get_db)):
    empleados_resumidos = listar_empleados_detalle(db=db, page=page, size=size)
    return empleados_resumidos


# ruta para listar todos los empleados activos
@router.get("/activos", response_model=List[EmpleadoRead])
def obtener_empleados_activos_endpoint(
    current_user: UsuarioRead = Depends(RoleChecker(VIEW_EMPLOYEE_ROLES)),
    page: int = Query(1, ge=1),
    size: int = Query(5, ge=1, le=100),     
    db: Session = Depends(get_db)):
    empleados_activos = listar_empleados_activos(db=db, page=page, size=size)
    return empleados_activos


# ruta para listar todos los empleados inactivos
@router.get("/inactivos", response_model=List[EmpleadoRead])
def obtener_empleados_inactivos_endpoint(
    current_user: UsuarioRead = Depends(RoleChecker(VIEW_EMPLOYEE_ROLES)),
    page: int = Query(1, ge=1),
    size: int = Query(5, ge=1, le=100),     
    db: Session = Depends(get_db)):
    empleados_inactivos = listar_empleados_inactivos(db=db, page=page, size=size)
    return empleados_inactivos


# ruta para obtener un empleado por su id
@router.get("/{id}", response_model=EmpleadoRead)
def obtener_empleado_id_detalle_endpoint(
    id: int = Path(..., gt=0, description="Id del empleado a consultar"),
    current_user: UsuarioRead = Depends(RoleChecker(ALL_ROLES)),
    db: Session = Depends(get_db)
):
    empleado = obtener_empleado_por_id(db, id)
    
    if not empleado:
        raise HTTPException(
            status_code=404,
            detail=f"Empleado con id {id} no encontrado"
        )
        
    return empleado


# ruta para editar un empleado por su id
@router.put("/{id}", response_model=EmpleadoRead, status_code=200)
def editar_empleado_endpoint(
    id: int = Path(..., gt=0, description="Id del empleado a editar"),
    datos: EmpleadoUpdate = None,
    current_user: UsuarioRead = Depends(RoleChecker(MANAGEMENT_ROLES)),
    db: Session = Depends(get_db)
):
    empleado_editar = editar_empleado(db, id, datos)
    
    if not empleado_editar:
        raise HTTPException(
            status_code=404,
            detail=f"Empleado con id {id} no encontrado"
        )
    
    return empleado_editar


# ruta para desactivar un empleado por su id
@router.patch("/{id}/desactivar", response_model=EmpleadoRead, status_code=200)
def desactivar_empleado_endpont(
    datos: EmpleadoDesactivar,
    id: int,
    current_user: UsuarioRead = Depends(RoleChecker(ADMIN_ONLY)),
    db: Session = Depends(get_db)
):
    empleado_desactivar = desactivar_empleado(db, id, datos)
    
    if not empleado_desactivar:
        raise HTTPException(
            status_code=404,
            detail=f"Empleado con id {id} no encontrado"
        )
        
    return empleado_desactivar




