from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from schemas.empleado import EmpleadoCreate, EmpleadoUpdate, EmpleadoDesactivar
from repositories.empleado_repository import EmpleadoRepository


# servicio para crear un empleado
def crear_empleado(db: Session, datos: EmpleadoCreate):
    repository = EmpleadoRepository(db)
    
    try:
        
        # transformacion de datos para limpieza y estandarizacion
        datos.nombres = datos.nombres.title()
        datos.apellidos = datos.apellidos.title()
        datos.email = datos.email.lower()
        
        nuevo_empleado = repository.create_empleado(datos)
        
        db.commit()
        db.refresh(nuevo_empleado)

        return nuevo_empleado
    
    except SQLAlchemyError as e:
        db.rollback()
        raise e
 
    
# servicio para listar los empleados
def listar_empleados_detalle(db: Session, page: int = 1, size: int = 5):
    repository = EmpleadoRepository(db)
    
    skip = (page -1) * size
    empleados = repository.get_empleados_all(skip=skip, limit=size)
    
    return empleados


# servicio para buscar un empleado por su id
def obtener_empleado_por_id(db: Session, id: int):
    repository = EmpleadoRepository(db)
    
    return repository.get_empleado(id)


# servicio para editar un empleado
def editar_empleado(db: Session, id: int, datos: EmpleadoUpdate):
    repository = EmpleadoRepository(db)
    
    empleado = repository.get_empleado(id)
    
    if not empleado:
        return None
    
    try:
        # actualizacion de datos segun sea necesarios
        if datos.nombres is not None:
            empleado.nombres = datos.nombres.title()
        if datos.apellidos is not None:
            empleado.apellidos = datos.apellidos.title()
        if datos.telefono is not None:
            empleado.telefono = datos.telefono
        if datos.email is not None:
            empleado.email = datos.email.lower()
        if datos.salario is not None:
            empleado.salario = datos.salario
        if datos.fecha_ingreso is not None:
            empleado.fecha_ingreso = datos.fecha_ingreso
        if datos.dependencia_id is not None:
            empleado.dependencia_id = datos.dependencia_id
        if datos.cargo_id is not None:
            empleado.cargo_id = datos.cargo_id
        
        db.commit()
        db.refresh(empleado)
        
        return empleado
    
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    

# servicio para desactivar un empleado segun fecha salida
def desactivar_empleado(db: Session, id: int, datos: EmpleadoDesactivar):
    repository = EmpleadoRepository(db)
    
    empleado = repository.get_empleado(id)
    
    if not empleado:
        return None
    
    try:
        if datos.fecha_salida is None:
            raise ValueError("La fecha de salida es obligatoria")
        if datos.fecha_salida < empleado.fecha_ingreso:
            raise ValueError("La fecha de salida no puede ser menor a la fecha de ingreso")
        
        empleado.fecha_salida = datos.fecha_salida
        empleado.activo = False
        
        db.commit()
        db.refresh(empleado)
        
        return empleado
    
    except SQLAlchemyError as e:
        db.rollback()
        raise e
    
    
# servicio para listar todos los empleados activos
def listar_empleados_activos(db: Session, page: int = 1, size: int = 5):
    repository = EmpleadoRepository(db)
    
    skip = (page - 1) * size
    
    return repository.get_empleados_activos(skip=skip, limit=size)


# servicio para listar todos los empleados inactivos
def listar_empleados_inactivos(db: Session, page: int = 1, size: int = 5):
    repository = EmpleadoRepository(db)
    
    skip = (page - 1) * size
    
    return repository.get_empleados_inactivos(skip=skip, limit=size)

    
