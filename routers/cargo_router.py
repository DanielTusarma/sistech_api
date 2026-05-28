from fastapi import APIRouter, Depends, HTTPException, Path, Query
from typing import List
from sqlalchemy.orm import Session

from database import get_db
from services.cargo_service import(
    crear_cargo,
    listar_cargos,
    listar_empleados_cargo,
    obtener_cargo_por_id
)
from schemas.cargo import CargoCreate, CargoRead
from schemas.empleado import EmpleadoRead

router = APIRouter(
    prefix="/api/cargos",
    tags=["Cargos"]
)

# ruta para crear un cargo
@router.post("/", response_model=CargoRead, status_code=201)
def crear_cargo_endpoint(datos: CargoCreate, db: Session = Depends(get_db)):
    # crear cargo
    nuevo_cargo = crear_cargo(db, datos)
    return nuevo_cargo

# ruta para listar todos los cargos
@router.get("/", response_model=List[CargoRead])
def listar_cargos_endpoint(
    page: int = Query(1, ge=1),
    size: int = Query(5, ge=1, le=100),
    db: Session = Depends(get_db)
):
    cargos = listar_cargos(db=db, page=page, size=size)
    return cargos

# ruta para listar los empleados por cargo
@router.get("/{id}/empleados", response_model=List[EmpleadoRead])
def listar_empleados_cargo_endpoint(
    id: int = Path(..., gt=0, description="Id del cargo a consultar"),
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
