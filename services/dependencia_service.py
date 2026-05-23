from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from schemas.dependencia import DependenciaCreate
from repositories.dependencia_repository import DependenciaRepository


# servicio para crear una nueva dependencia
def crear_dependencia(db: Session, datos: DependenciaCreate):
    repository = DependenciaRepository(db)
    
    try:
        
        nueva_dependencia = repository.create_dependencia(datos.nombre.title())
        
        db.commit()
        db.refresh(nueva_dependencia)
        
        return nueva_dependencia
    
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    
# servicio para listar todas las dependencias
def listar_dependencias(db: Session):
    repository = DependenciaRepository(db)
    
    return repository.get_dependencias_all()
    
    
        