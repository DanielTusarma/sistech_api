from fastapi import APIRouter, Depends, HTTPException, Path
from typing import List
from sqlalchemy.orm import Session

from database import get_db
from services.dependencia_service import(
    crear_dependencia,
    listar_dependencias
)
from schemas.dependencia import DependenciaCreate, DependenciaRead

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
    



