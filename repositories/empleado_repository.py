from sqlalchemy.orm import Session
from models.empleado import Empleado
from schemas.empleado import EmpleadoCreate, EmpleadoUpdate
from datetime import date

class EmpleadoRepository:
    # Repositorio para manejar las operaciones relacionadas con la entidad Empleado
    def __init__(self, db: Session):
        self.db = db
        
    # Obtener un empleado por su id
    def get_empleado(self, empleado_id: int) -> Empleado | None:
        empleado = self.db.query(Empleado).filter(Empleado.id==empleado_id).first()
        return empleado
    
    # Crear un empleado nuevo
    def create_empleado(self, datos: EmpleadoCreate) -> Empleado:
        nuevo_empleado = Empleado(**datos.model_dump())
        self.db.add(nuevo_empleado)
        return nuevo_empleado
    
    # Listar todos los empleados
    def get_empleados_all(self, skip: int = 0, limit: int = 5) -> list[Empleado]:
        empleados = self.db.query(Empleado).order_by(Empleado.id).offset(skip).limit(limit).all()
        return empleados
    
    # editar un empleado existente
    def update_empleado(self, empleado_id: int, datos: EmpleadoUpdate) -> Empleado | None:
        empleado = self.get_empleado(empleado_id)
        if empleado:
            for key, value in datos.model_dump(exclude_unset=True).items():
                setattr(empleado, key, value)
        return empleado
    

    # desactivar un empleado (marcarlo como inactivo)
    def desactivar_empleado(self, empleado_id: int, fecha_salida: date) -> Empleado | None:
        empleado = self.get_empleado(empleado_id)
        if empleado:
            empleado.activo = False
            empleado.fecha_salida = fecha_salida
        return empleado
    
    # listar empleados activos
    def get_empleados_activos(self, skip: int = 0, limit: int = 5) -> list[Empleado]:
        empleados_activos = self.db.query(Empleado).filter(Empleado.activo==True).order_by(Empleado.id).offset(skip).limit(limit).all()
        return empleados_activos
    
    # listar empleados inactivos
    def get_empleados_inactivos(self, skip: int = 0, limit: int = 5) -> list[Empleado]:
        empleados_inactivos = self.db.query(Empleado).filter(Empleado.activo==False).order_by(Empleado.id).offset(skip).limit(limit).all()
        return empleados_inactivos
    
    # listar empleados por dependencia
    def get_empleados_por_dependencia(self, dependencia_id: int, skip: int = 0, limit: int = 5) -> list[Empleado]:
        empleados_dependencia = self.db.query(Empleado).filter(Empleado.dependencia_id==dependencia_id).order_by(Empleado.id).offset(skip).limit(limit).all()
        return empleados_dependencia
    
    # listar empleados por cargo
    def get_empleados_por_cargo(self, cargo_id: int, skip: int = 0, limit: int = 5) -> list[Empleado]:
        empleados_cargo = self.db.query(Empleado).filter(Empleado.cargo_id==cargo_id).order_by(Empleado.id).offset(skip).limit(limit).all()
        return empleados_cargo
    
    
    """
    Funciones para contar empleados segun necesidades varias
    """
    
    # contar los empleados activos
    def count_empleados_activos(self):
        return(self.db.query(Empleado).filter(Empleado.activo==True).count())
        
    # contar los empleados inactivos
    def count_empleados_inactivos(self):
        return(self.db.query(Empleado).filter(Empleado.activo==False).count())

    # contar todos los empleados
    def count_empleados_all(self):
        return(self.db.query(Empleado).count())
    
    # contar empleados por dependencia
    def count_empleados_por_dependencia(self, dependencia_id: int):
        return(self.db.query(Empleado).filter(Empleado.dependencia_id==dependencia_id).count())

    # contar empleados por cargo
    def count_empleados_por_cargo(self, cargo_id: int):
        return(self.db.query(Empleado).filter(Empleado.cargo_id==cargo_id).count())