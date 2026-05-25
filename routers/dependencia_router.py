from fastapi import APIRouter, Depends, HTTPException, Path
from typing import List
from sqlalchemy.orm import Session

from database import get_db
from services.dependencia_service import(
    crear_dependencia,
    listar_dependencias,
    listar_empleados_dependencia
)
from schemas.dependencia import DependenciaCreate, DependenciaRead
from schemas.empleado import EmpleadoRead

router = APIRouter(
    prefix="/api/dependencias",
    tags=["Dependencias"]
)

# ruta para crear una dependencia
@router.post("/", response_model=DependenciaRead, status_code=201)
def crear_dependencia_endpoint(datos: DependenciaCreate, db: Session = Depends(get_db)):
    # crear dependencia
    nueva_dependencia = crear_dependencia(db, datos)
    return nueva_dependencia

# ruta para listar todas las dependencias
@router.get("/", response_model=List[DependenciaRead])
def listar_dependencias_endpoint(db: Session = Depends(get_db)):
    dependencias = listar_dependencias(db)
    return dependencias


# ruta para listar los empleados por dependencia
@router.get("/{id}/empleados", response_model=List[EmpleadoRead])
def listar_empleados_dependencia_endpoint(
    id: int = Path(..., gt=0, description="Id de la dependencia a consultar"),
    db: Session = Depends(get_db)
):
    dependencia = listar_empleados_dependencia(db, id)
    
    if not dependencia:
        raise HTTPException(
            status_code=404,
            detail=f"Dependencia con Id {id} no encontrada"
        )
    
    return dependencia
    
    
    



