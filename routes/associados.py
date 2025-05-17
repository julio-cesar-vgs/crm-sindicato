from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from models.associados import Associado
from schemas.associados import AssociadoCreate, AssociadoUpdate, AssociadoResponse
from database import get_db
# from utils import parse_date # Se parse_date for necessário, importe aqui

router = APIRouter()

@router.get("/", response_model=List[AssociadoResponse], summary="Lista todos os associados")
def list_associados(db: Session = Depends(get_db)):
    associados = db.query(Associado).all()
    return associados

@router.get("/{associado_id}", response_model=AssociadoResponse, summary="Obtém um associado por ID")
def get_associado(associado_id: int, db: Session = Depends(get_db)):
    associado = db.query(Associado).filter(Associado.id_associado == associado_id).first()
    if associado is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Associado não encontrado")
    return associado

@router.get("/count", summary="Conta o número total de associados")
def count_associados(db: Session = Depends(get_db)):
    try:
        count = db.query(Associado).count()
        return {"count": count}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.post("/", response_model=AssociadoResponse, status_code=status.HTTP_201_CREATED, summary="Cria um novo associado")
def create_associado(associado: AssociadoCreate, db: Session = Depends(get_db)):
    # Verificar se CNPJ já existe (opcional, mas recomendado)
    db_associado = db.query(Associado).filter(Associado.cnpj == associado.cnpj).first()
    if db_associado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="CNPJ já cadastrado")
    
    db_associado = Associado(**associado.dict())
    db.add(db_associado)
    db.session.commit()
    db.session.refresh(db_associado)
    return db_associado

@router.put("/{associado_id}", response_model=AssociadoResponse, summary="Atualiza um associado por ID")
def update_associado(associado_id: int, associado_update: AssociadoUpdate, db: Session = Depends(get_db)):
    db_associado = db.query(Associado).filter(Associado.id_associado == associado_id).first()
    if db_associado is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Associado não encontrado")
    
    update_data = associado_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_associado, field, value)

    db.session.commit()
    db.session.refresh(db_associado)
    return db_associado

@router.delete("/{associado_id}", status_code=status.HTTP_200_OK, summary="Deleta um associado por ID")
def delete_associado(associado_id: int, db: Session = Depends(get_db)):
    db_associado = db.query(Associado).filter(Associado.id_associado == associado_id).first()
    if db_associado is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Associado não encontrado")
    
    db.delete(db_associado)
    db.session.commit()
    return {"detail": "Associado removido com sucesso"}
