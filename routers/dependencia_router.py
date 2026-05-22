from fastapi import APIRouter, Depends, HTTPException, Path
from typing import List
from sqlalchemy.orm import Session

from database import get_db
from services.dependencia_service import(
    crear_dependencia
)
from schemas.dependencia import DependenciaCreate, DependenciaRead

router = APIRouter(
    prefix="/api/dependencias",
    tags=["Dependencias"]
)

# ruta para crear una dependencia
@router.post("/", response_model=DependenciaRead, status_code=201)
def crear_dependencia_emdpoint(datos: DependenciaCreate, db: Session = Depends(get_db)):
    # crear dependencia
    nueva_dependencia = crear_dependencia(db, datos)
    return nueva_dependencia



