from sqlalchemy.orm import Session
from models.dependencia import Dependencia

class DependenciaRepository:
    # Repositorio para manejar las operaciones relacionadas con la entidad Dependencia
    def __init__(self, db: Session):
        self.db = db
    
    # Obtener una dependencia por su id
    def get_dependencia(self, dependencia_id: int) -> Dependencia | None:
        dependencia = self.db.query(Dependencia).filter(Dependencia.id == dependencia_id).first()
        return dependencia
    
    # Crear una nueva dependencia
    def create_dependencia(self, nombre: str) -> Dependencia:
        nueva_dependencia = Dependencia(nombre=nombre)
        self.db.add(nueva_dependencia)
        return nueva_dependencia
    
    # obtener todas la dependencias
    def get_dependencias_all(self, skip: int = 0, limit: int = 5) -> list[Dependencia]:
        dependencias = self.db.query(Dependencia).order_by(Dependencia.id).offset(skip).limit(limit).all()
        return dependencias
    
    # contar las dependencias
    def count_dependencias(self):
        return(self.db.query(Dependencia).count())
    
    