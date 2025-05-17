from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# Schema Base (campos comuns)
class EventoBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    data_evento: datetime
    local: Optional[str] = None

# Schema para criação (todos os campos necessários para criar)
class EventoCreate(EventoBase):
    pass

# Schema para atualização (campos opcionais para atualizar)
class EventoUpdate(EventoBase):
    titulo: Optional[str] = None
    data_evento: Optional[datetime] = None

# Schema para resposta (campos retornados pela API, incluindo o ID e talvez participantes)
class EventoResponse(EventoBase):
    id_evento: int # Adicione o campo de ID do modelo Evento
    # Se você tiver uma relação com Participacoes, pode adicionar aqui:
    # participantes: List[ParticipacaoResponse] = [] # Assumindo que você tem um schema ParticipacaoResponse

    class Config:
        orm_mode = True # Permite que o Pydantic leia dados de modelos ORM (SQLAlchemy)
