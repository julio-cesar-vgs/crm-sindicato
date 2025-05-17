from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Schema Base (campos comuns)
class ContribuicaoBase(BaseModel):
    id_associado: int
    valor: float
    data_pagamento: Optional[datetime] = None
    status_pagamento: Optional[str] = None

# Schema para criação (todos os campos necessários para criar)
class ContribuicaoCreate(ContribuicaoBase):
    pass

# Schema para atualização (campos opcionais para atualizar)
class ContribuicaoUpdate(ContribuicaoBase):
    id_associado: Optional[int] = None
    valor: Optional[float] = None
    data_pagamento: Optional[datetime] = None
    status_pagamento: Optional[str] = None

# Schema para resposta (campos retornados pela API, incluindo o ID)
class ContribuicaoResponse(ContribuicaoBase):
    id_contribuicao: int # Adicione o campo de ID do modelo

    class Config:
        orm_mode = True # Permite que o Pydantic leia dados de modelos ORM (SQLAlchemy)
