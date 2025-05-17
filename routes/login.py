from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List

from models.login import Login
from schemas.login import LoginCreate, LoginUpdatePassword, Login as LoginSchema
from database import get_db

router = APIRouter()

@router.post("/", response_model=LoginSchema)
def create_login(user: LoginCreate, db: Session = Depends(get_db)):
    db_user = Login(nome=user.nome, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/", response_model=List[LoginSchema])
def read_logins(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(Login).offset(skip).limit(limit).all()
    return users

@router.get("/{user_id}", response_model=LoginSchema)
def read_login(user_id: int, db: Session = Depends(get_db)):
    user = db.query(Login).filter(Login.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=LoginSchema)
def update_login_password(user_id: int, user_update: LoginUpdatePassword, db: Session = Depends(get_db)):
    db_user = db.query(Login).filter(Login.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.password = user_update.password
    db_user.updateAt = datetime.now()
    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete("/{user_id}", response_model=LoginSchema)
def delete_login(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(Login).filter(Login.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return db_user
