from fastapi import HTTPException, status, Depends
from models.enum import RolUsuario
from .dependencies import get_current_user
from schemas.usuario import UsuarioRead

# grupos de permisos reutilizabes 

# solo admin puede acceder a ciertas rutas
ADMIN_ONLY = [RolUsuario.ADMIN]

# solo admin y supervisor pueden acceder a ciertas rutas
MANAGEMENT_ROLES = [RolUsuario.ADMIN, RolUsuario.SUPERVISOR]

# admin, supervisor y auditor pueden acceder a ciertas rutas
VIEW_EMPLOYEE_ROLES = [RolUsuario.ADMIN, RolUsuario.SUPERVISOR, RolUsuario.AUDITOR]

# todos los roles pueden acceder a ciertas rutas
ALL_ROLES = [RolUsuario.ADMIN, RolUsuario.USUARIO, RolUsuario.SUPERVISOR, RolUsuario.AUDITOR]


class RoleChecker:
    def __init__(self, allowed_roles: list[RolUsuario]):
        self.allowed_roles = allowed_roles
        
    def __call__(self, current_user: UsuarioRead = Depends(get_current_user)):
        if current_user.rol not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Operación no permitida: permisos insuficientes"
            )
        return current_user
