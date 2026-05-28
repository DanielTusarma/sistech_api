from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from schemas.dependencia import DependenciaCreate
from repositories.dependencia_repository import DependenciaRepository
from repositories.empleado_repository import EmpleadoRepository


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
def listar_dependencias(db: Session, page: int = 1, size: int = 5):
    repository = DependenciaRepository(db)
    
    skip = (page - 1) * size
    
    return repository.get_dependencias_all(skip=skip, limit=size)


# servicio para listar los empleados por dependencia
def listar_empleados_dependencia(db: Session, id_dependencia: int, page: int = 1, size: int = 5):
    repository = EmpleadoRepository(db)
    
    skip = (page - 1) * size
    
    return repository.get_empleados_por_dependencia(id_dependencia, skip=skip, limit=size)
    

# servicio para obtener una dependencia por su id
def obtener_dependencia_por_id(db: Session, id: int):
    repository = DependenciaRepository(db)
    
    return repository.get_dependencia(id)