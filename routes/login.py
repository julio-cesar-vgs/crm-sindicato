from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List

from models.login import Login # Importe o modelo Login diretamente
from schemas.login import LoginCreate, LoginUpdatePassword, Login as LoginSchema # Importe os schemas LoginCreate, LoginUpdatePassword, e renomeie o schema Login para evitar conflito com o modelo
from database import get_db # Importe a função get_db

router = APIRouter()

@router.post("/", response_model=LoginSchema) # Use o schema renomeado para resposta
def create_login(user: LoginCreate, db: Session = Depends(get_db)): # Use os schemas importados diretamente
    db_user = Login(nome=user.nome, password=user.password) # createAt defaults in model # Use o modelo Login importado diretamente
    db.refresh(db_user)
    return db_user

@router.get("/", response_model=List[schemas.Login])
def read_logins(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(models.Login).offset(skip).limit(limit).all()
    return users

@router.get("/{user_id}", response_model=schemas.Login)
def read_login(user_id: int, db: Session = Depends(get_db)):
    user = db.query(Login).filter(Login.id == user_id).first() # Use o modelo Login importado diretamente
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put(\"/{user_id}\", response_model=LoginSchema) # Use o schema renomeado para resposta
def update_login_password(user_id: int, user_update: LoginUpdatePassword, db: Session = Depends(get_db)): # Use os schemas importados diretamente
    db_user = db.query(Login).filter(Login.id == user_id).first() # Use o modelo Login importado diretamente
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db_user.password = user_update.password
    db_user.updateAt = datetime.now()

    return db_user

@router.delete(\"/{user_id}\", response_model=LoginSchema) # Use o schema renomeado para resposta
def delete_login(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(Login).filter(Login.id == user_id).first() # Use o modelo Login importado diretamente
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(db_user)
    db.commit()
    return db_user