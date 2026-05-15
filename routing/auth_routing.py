from fastapi import APIRouter, Depends
from models import RegisterRequest, LoginRequest
from data.db import get_db
from schema.user_schema import User
from helpers.password import hash_password, verify_password, create_access_token
from typing import Annotated
from sqlalchemy.orm import Session

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.post("/register")
def register(data: RegisterRequest, db: Annotated[Session, Depends(get_db)]):
    user = db.query(User).filter(User.email == data.email).first()
    if user:
        return {"message": "Email already registered"}
    new_user = User(name=data.name, email=data.email, hashed_password=hash_password(data.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}


@router.post("/login")
def login(data: LoginRequest, db: Annotated[Session, Depends(get_db)]):
    user = db.query(User).filter(User.email == data.email).first()
    if not user:
        return {"message": "Invalid email or password"}
    if not verify_password(data.password, user.hashed_password):
        return {"message": "Invalid email or password"}
    payload = {"user_id": user.id, "email": user.email}
    token = create_access_token(payload)
    payload["token"] = "Bearer " + token
    return {"message": "Login successful", "data": payload}