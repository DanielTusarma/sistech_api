from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from schemas.cargo import CargoCreate
from repositories.cargo_repository import CargoRepository
from repositories.empleado_repository import EmpleadoRepository


# servicio para crear un nuevo cargo
def crear_cargo(db: Session, datos: CargoCreate):
    repository = CargoRepository(db)
    
    try:
        
        # transformacion de datos para estandarizacion
        datos.nombre = datos.nombre.title()
        
        
        nuevo_cargo = repository.create_cargo(datos)
        
        db.commit()
        db.refresh(nuevo_cargo)
        
        return nuevo_cargo
    
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    

# servicio para listar todos los cargos
def listar_cargos(db: Session, page: int = 1, size: int = 5):
    repository = CargoRepository(db)
    
    skip = (page - 1) * size
    
    return repository.get_cargos_all(skip=skip, limit=size)


# servicio para listar los empleados por cargo
def listar_empleados_cargo(db: Session, id_cargo: int, page: int = 1, size: int = 5):
    repository = EmpleadoRepository(db)
    
    skip = (page - 1) * size
    
    return repository.get_empleados_por_cargo(id_cargo, skip=skip, limit=size)

# servicio para obtener un cargo por su id
def obtener_cargo_por_id(db: Session, id: int):
    repository = CargoRepository(db)
    
    return repository.get_cargo(id)
    
    