from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from models.interacoes import Interacao  # Importe seu modelo Interacao
from schemas.interacoes import InteracaoCreate, InteracaoUpdate, InteracaoResponse  # Importe seus schemas Pydantic
from database import get_db  # Importe a função get_db
# Se você usava parse_date aqui e ainda precisa dele, importe-o:
# from utils import parse_date

router = APIRouter()

@router.get(
    "/",
    response_model=List[InteracaoResponse],
    summary="Lista todas as interações",
    description="Retorna uma lista de todas as interações registradas."
)
def list_interacoes(db: Session = Depends(get_db)):
    interacoes = db.query(Interacao).all()
    return interacoes

@router.get(
    "/{id}",
    response_model=InteracaoResponse,
    summary="Obtém uma interação por ID",
    description="Retorna os detalhes de uma interação específica pelo seu ID."
)
def get_interacao(id: int, db: Session = Depends(get_db)):
    interacao = db.query(Interacao).filter(Interacao.id_interacao == id).first()
    if interacao is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Interação não encontrada")
    return interacao

@router.post(
    "/",
    response_model=InteracaoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cria uma nova interação",
    description="Cria uma nova entrada de interação no sistema."
)
def create_interacao(interacao: InteracaoCreate, db: Session = Depends(get_db)):
    # Adapte a criação para usar o schema Pydantic
    # Se 'data_interacao' precisa de parse_date, use: data_interacao=parse_date(interacao.data_interacao)
    db_interacao = Interacao(**interacao.dict())
    db.add(db_interacao)
    db.commit()
    db.refresh(db_interacao)
    return db_interacao

@router.put(
    "/{id}",
    response_model=InteracaoResponse,
    summary="Atualiza uma interação por ID",
    description="Atualiza os detalhes de uma interação específica pelo seu ID."
)
def update_interacao(id: int, interacao_update: InteracaoUpdate, db: Session = Depends(get_db)):
    db_interacao = db.query(Interacao).filter(Interacao.id_interacao == id).first()
    if db_interacao is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Interação não encontrada")

    # Adapte a atualização para usar o schema Pydantic e atualizar apenas os campos fornecidos
    update_data = interacao_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_interacao, field, value)

    db.commit()
    db.refresh(db_interacao)
    return db_interacao

@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    summary="Deleta uma interação por ID",
    description="Remove uma interação específica pelo seu ID."
)
def delete_interacao(id: int, db: Session = Depends(get_db)):
    db_interacao = db.query(Interacao).filter(Interacao.id_interacao == id).first()
    if db_interacao is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Interação não encontrada")

    db.delete(db_interacao)
    db.commit()
    return {"detail": "Interação removida com sucesso"} # Retorno HTTP 200 com mensagem

@interacoes_bp.route('/count', methods=['GET'])
def count_interacoes():
    try:
        count = Interacao.query.count()
        return jsonify({"count": count}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
