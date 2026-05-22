from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from schemas.dependencia import DependenciaCreate, DependenciaRead
from repositories.dependencia_repository import DependenciaRepository


# servicio para crear una nueva dependencia
def crear_dependencia(db: Session, datos: DependenciaCreate):
    repository = DependenciaRepository(db)
    
    try:
        
        nueva_dependencia = repository.create_dependencia(datos.nombre)
        
        db.commit()
        db.refresh(nueva_dependencia)
        
        return nueva_dependencia
    
    except SQLAlchemyError as e:
        db.rollback()
        raise e