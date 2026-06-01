# Archivo encargado de funciones de seguridad y criptografía.
# Aquí se manejan hashes de contraseñas, creación y validación de JWT.
# No debe contener lógica HTTP ni acceso directo a rutas.

from passlib.context import CryptContext
import os
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from dotenv import load_dotenv

# cargar las variables de entorno
load_dotenv()

HASH_SCHEME = "argon2"
SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES", "30"))

pwd_context = CryptContext(schemes=[HASH_SCHEME], deprecated="auto")

# hash de contraseña
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# verificación de contraseña
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# creación de token JWT
def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)   

# verificación de token JWT
def verify_access_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise JWTError("Token inválido o expirado")


    