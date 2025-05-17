from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from models.eventos import Evento # Importe seu modelo Evento
from schemas.eventos import EventoCreate, EventoUpdate, EventoResponse # Importe os schemas Pydantic que você acabou de criar
from database import get_db # Importe a função get_db
# Se você usava parse_date aqui e ainda precisa dele, importe-o:
# from utils import parse_date

router = APIRouter()

@router.get(
    "/",
    response_model=List[EventoResponse],
    summary="Lista todos os eventos",
    description="Retorna uma lista de todos os eventos registrados."
)
def list_eventos(db: Session = Depends(get_db)):
    eventos = db.query(Evento).all()
    return eventos

@router.get(
    "/{id}",
    response_model=EventoResponse,
    summary="Obtém um evento por ID",
    description="Retorna os detalhes de um evento específico pelo seu ID."
)
def get_evento(id: int, db: Session = Depends(get_db)):
    evento = db.query(Evento).filter(Evento.id_evento == id).first()
    if evento is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evento não encontrado")
    return evento

@router.post(
    "/",
    response_model=EventoResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cria um novo evento",
    description="Cria uma nova entrada de evento no sistema."
)
def create_evento(evento: EventoCreate, db: Session = Depends(get_db)):
    # Adapte a criação para usar o schema Pydantic
    # Se 'data_evento' precisa de parse_date, use: data_evento=parse_date(evento.data_evento)
    db_evento = Evento(**evento.dict())
    db.add(db_evento)
    db.commit()
    db.refresh(db_evento)
    return db_evento

@router.put(
    "/{id}",
    response_model=EventoResponse,
    summary="Atualiza um evento por ID",
    description="Atualiza os detalhes de um evento específico pelo seu ID."
)
def update_evento(id: int, evento_update: EventoUpdate, db: Session = Depends(get_db)):
    db_evento = db.query(Evento).filter(Evento.id_evento == id).first()
    if db_evento is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evento não encontrado")

    # Adapte a atualização para usar o schema Pydantic e atualizar apenas os campos fornecidos
    update_data = evento_update.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_evento, field, value)

    db.commit()
    db.refresh(db_evento)
    return db_evento

@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    summary="Deleta um evento por ID",
    description="Remove um evento específico pelo seu ID."
)
def delete_evento(id: int, db: Session = Depends(get_db)):
    db_evento = db.query(Evento).filter(Evento.id_evento == id).first()
    if db_evento is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Evento não encontrado")

    db.delete(db_evento)
    db.commit()
    return {"detail": "Evento removido com sucesso"} # Retorno HTTP 200 com mensagem

# Se você tinha uma rota de contagem para eventos, adicione-a aqui:
# @router.get("/count", summary="Conta o número total de eventos")
# def count_eventos(db: Session = Depends(get_db)):
#     try:
#         count = db.query(Evento).count()
#         return {"count": count}
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
