from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from models.contribuicoes import Contribuicao # Importe seu modelo Contribuicao
from schemas.contribuicoes import ContribuicaoCreate, ContribuicaoUpdate, ContribuicaoResponse # Importe seus schemas Pydantic
from database import get_db # Importe a função get_db

router = APIRouter()

@router.get(
    "/",
    response_model=List[ContribuicaoResponse],
    summary="Lista todas as contribuições",
    description="Retorna uma lista de todas as contribuições registradas."
)
def list_contribuicoes(db: Session = Depends(get_db)):
    contribuicoes = db.query(Contribuicao).all()
    return contribuicoes

@router.get(
    "/{id}",
    response_model=ContribuicaoResponse,
    summary="Obtém uma contribuição por ID",
    description="Retorna os detalhes de uma contribuição específica pelo seu ID."
)
def get_contrib(id: int, db: Session = Depends(get_db)):
    contribuicao = db.query(Contribuicao).filter(Contribuicao.id_contribuicao == id).first()
    if contribuicao is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contribuição não encontrada")
    return contribuicao

@router.get(
    "/count",
    summary="Conta o número total de contribuições",
    description="Retorna o número total de contribuições registradas."
)
def count_contribuicoes(db: Session = Depends(get_db)):
    try:
        count = db.query(Contribuicao).count()
        return {"count": count}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.post(
    "/",
    response_model=ContribuicaoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cria uma nova contribuição",
    description="Cria uma nova entrada de contribuição no sistema."
)
def create_contrib(contribuicao: ContribuicaoCreate, db: Session = Depends(get_db)):
    # Adapte a criação para usar o schema Pydantic
    db_contribuicao = Contribuicao(**contribuicao.dict())
    db.add(db_contribuicao)
    db.commit()
    db.refresh(db_contribuicao)
    return db_contribuicao

@router.put(
    "/{id}",
    response_model=ContribuicaoResponse,
    summary="Atualiza uma contribuição por ID",
    description="Atualiza os detalhes de uma contribuição específica pelo seu ID."
)
def update_contrib(id: int, contribuicao_update: ContribuicaoUpdate, db: Session = Depends(get_db)):
    db_contribuicao = db.query(Contribuicao).filter(Contribuicao.id_contribuicao == id).first()
    if db_contribuicao is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contribuição não encontrada")

    # Adapte a atualização para usar o schema Pydantic e atualizar apenas os campos fornecidos
    update_data = contribuicao_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_contribuicao, field, value)

    db.commit()
    db.refresh(db_contribuicao)
    return db_contribuicao

@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    summary="Deleta uma contribuição por ID",
    description="Remove uma contribuição específica pelo seu ID."
)
def delete_contrib(id: int, db: Session = Depends(get_db)):
    db_contribuicao = db.query(Contribuicao).filter(Contribuicao.id_contribuicao == id).first()
    if db_contribuicao is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contribuição não encontrada")

    db.delete(db_contribuicao)
    db.commit()
    return {"detail": "Contribuição removida com sucesso"} # Retorno HTTP 200 com mensagem
