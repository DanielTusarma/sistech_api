# Archivo encargado de manejar las rutas relacionadas con autenticación.
# Aquí se definen endpoints como login, logout o refresh token.
# Su responsabilidad es recibir requests HTTP y comunicarse con los servicios auth.

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from .auth_services import login_user
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/api/auth",
    tags=["Auth"]
)


@router.post("/login", status_code=200)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario_login = login_user(db, form_data.username, form_data.password)
    return usuario_login