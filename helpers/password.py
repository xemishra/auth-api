from pwdlib import PasswordHash
import jwt
from config.app_config import get_app_config
from datetime import datetime, timedelta, timezone

def hash_password(password: str) -> str:
    ph = PasswordHash.recommended()
    return ph.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    ph = PasswordHash.recommended()
    return ph.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    config = get_app_config()
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=config.access_token_expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.secret_key, algorithm=config.algorithm)
    return encoded_jwt

def decode_access_token(token: str) -> dict:
    config = get_app_config()
    payload = jwt.decode(token, config.secret_key, algorithms=[config.algorithm])
    return payload