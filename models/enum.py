from enum import Enum

class RolUsuario(str, Enum):
    ADMIN = "admin"
    USUARIO = "usuario"
    SUPERVISOR = "supervisor"