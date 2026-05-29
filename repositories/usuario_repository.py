from sqlalchemy.orm import Session
from models.usuario import Usuario
from schemas.usuario import UsuarioCreate

class UsuarioRepository:
    # Repositorio para manejas las relaciones con la entidad usuario
    def __init__(self, db: Session):
        self.db = db
        
    # Obtener un usuario por su id
    def get_usuario(self, usuario_id: int) -> Usuario | None:
        usuario = self.db.query(Usuario).filter(Usuario.id==usuario_id).first()
        return usuario
    
    # Crear un nuevo usuario
    def create_usuario(self, datos: dict) -> Usuario:
        nuevo_usuario = Usuario(**datos)
        self.db.add(nuevo_usuario)
        return nuevo_usuario
    
    # Obtener un usuario por su email
    def get_usuario_email(self, email: str) -> Usuario | None:
        usuario_email = self.db.query(Usuario).filter(Usuario.email==email).first()
        return usuario_email
    
    # Listar todos los usuarios
    def get_usuarios_all(self, skip: int = 0, limit: int = 5) -> list[Usuario]:
        usuarios = self.db.query(Usuario).order_by(Usuario.id).offset(skip).limit(limit).all()
        return usuarios
