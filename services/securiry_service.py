from passlib.context import CryptContext

HASH_SCHEME = "argon2"

pwd_context = CryptContext(schemes=[HASH_SCHEME], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)


