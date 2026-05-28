from sqlalchemy.orm import Session
from models.cargo import Cargo
from schemas.cargo import CargoCreate

class CargoRepository:
    # Repositorio para manejar las operaciones con la entidad Cargo
    def __init__(self, db: Session):
        self.db = db
        
    # Obtener un cargo por su id
    def get_cargo(self, cargo_id: int) -> Cargo | None:
        cargo = self.db.query(Cargo).filter(Cargo.id == cargo_id).first()
        return cargo
    
    # Crear un nuevo cargo
    def create_cargo(self, datos: CargoCreate) -> Cargo:
        nuevo_cargo = Cargo(**datos.model_dump())
        self.db.add(nuevo_cargo)
        return nuevo_cargo
    
    # obtener todos los cargos
    def get_cargos_all(self, skip: int = 0, limit: int = 5) -> list[Cargo]:
        cargos = self.db.query(Cargo).order_by(Cargo.id).offset(skip).limit(limit).all()
        return cargos