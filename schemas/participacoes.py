from pydantic import BaseModel
from typing import Optional

# Schema Base (campos comuns)
class ParticipacaoBase(BaseModel):
    id_evento: int
    id_associado: int
    feedback: Optional[str] = None

# Schema para criação (todos os campos necessários para criar)
class ParticipacaoCreate(ParticipacaoBase):
    pass

# Schema para atualização (campos opcionais para atualizar)
class ParticipacaoUpdate(ParticipacaoBase):
    id_evento: Optional[int] = None
    id_associado: Optional[int] = None
    feedback: Optional[str] = None

# Schema para resposta (campos retornados pela API, incluindo o ID)
class ParticipacaoResponse(ParticipacaoBase):
    id_participacao: int # Adicione o campo de ID do modelo Participacao

    class Config:
        orm_mode = True # Permite que o Pydantic leia dados de modelos ORM (SQLAlchemy)