from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Schema Base (campos comuns)
class InteracaoBase(BaseModel):
    id_associado: int
    tipo_interacao: str
    data_interacao: datetime
    resumo: Optional[str] = None

# Schema para criação (todos os campos necessários para criar)
class InteracaoCreate(InteracaoBase):
    pass

# Schema para atualização (campos opcionais para atualizar)
class InteracaoUpdate(InteracaoBase):
    id_associado: Optional[int] = None
    tipo_interacao: Optional[str] = None
    data_interacao: Optional[datetime] = None
    resumo: Optional[str] = None

# Schema para resposta (campos retornados pela API, incluindo o ID)
class InteracaoResponse(InteracaoBase):
    id_interacao: int  # Adicione o campo de ID do modelo Interacao

    class Config:
        orm_mode = True  # Permite que o Pydantic leia dados de modelos ORM (SQLAlchemy)