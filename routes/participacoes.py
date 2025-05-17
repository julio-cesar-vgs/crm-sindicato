from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel # Certifique-se de importar BaseModel do pydantic

from models.participacoes import Participacao  # Importe seu modelo Participacao
from schemas.participacoes import ParticipacaoCreate, ParticipacaoUpdate, ParticipacaoResponse  # Importe seus schemas Pydantic
class ParticipacaoBase(BaseModel):
    id_evento: int
    id_associado: int
    feedback: Optional[str] = None

class ParticipacaoCreate(ParticipacaoBase):
    pass

class ParticipacaoUpdate(ParticipacaoBase):
    id_evento: Optional[int] = None
    id_associado: Optional[int] = None

class ParticipacaoResponse(ParticipacaoBase):
    id_participacao: int

    class Config:
        orm_mode = True

from database import get_db  # Importe a função get_db
router = APIRouter()


@router.get(
    "/",
    response_model=List[ParticipacaoResponse],
    summary="Lista todas as participações",
    description="Retorna uma lista de todas as participações registradas em eventos."
)
def list_participacoes(db: Session = Depends(get_db)):
    participacoes = db.query(Participacao).all()
    return participacoes


@router.get(
    "/{id}",
    response_model=ParticipacaoResponse,
    summary="Obtém uma participação por ID",
    description="Retorna os detalhes de uma participação específica pelo seu ID."
)
def get_participacao(id: int, db: Session = Depends(get_db)):
    participacao = db.query(Participacao).filter(Participacao.id_participacao == id).first()
    if participacao is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Participação não encontrada")
    return participacao


@router.post(
    "/",
    response_model=ParticipacaoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cria uma nova participação",
    description="Registra a participação de um associado em um evento."
)
def create_participacao(participacao: ParticipacaoCreate = Body(...), db: Session = Depends(get_db)):
    try:
        db_participacao = Participacao(**participacao.dict())
        db.add(db_participacao)
        db.commit()
        db.refresh(db_participacao)
        return db_participacao
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get(
    "/count",
    summary="Conta o número total de participações",
    description="Retorna o número total de participações registradas."
)
def count_participacoes(db: Session = Depends(get_db)):
    try:
        count = Participacao.query.count()
        return {"count": count}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.put(
    "/{id}",
    response_model=ParticipacaoResponse,
    summary="Atualiza uma participação por ID",
    description="Atualiza os detalhes de uma participação específica pelo seu ID."
)
def update_participacao(id: int, participacao_update: ParticipacaoUpdate = Body(...), db: Session = Depends(get_db)):
    db_participacao = db.query(Participacao).filter(Participacao.id_participacao == id).first()
    if db_participacao is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Participação não encontrada")

    update_data = participacao_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_participacao, field, value)

    db.commit()
    db.refresh(db_participacao)
    return db_participacao


@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    summary="Deleta uma participação por ID",
    description="Remove uma participação específica pelo seu ID."
)
def delete_participacao(id: int, db: Session = Depends(get_db)):
    db_participacao = db.query(Participacao).filter(Participacao.id_participacao == id).first()
    if db_participacao is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Participação não encontrada")

    db.delete(db_participacao)
    db.commit()
    return {"detail": "Participação removida com sucesso"}
