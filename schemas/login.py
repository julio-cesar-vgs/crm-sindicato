from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Schema Base (campos comuns)
class LoginBase(BaseModel):
    nome: str

# Schema para criação (com nome e password)
class LoginCreate(LoginBase):
    password: str

# Schema para atualização de senha
class LoginUpdatePassword(BaseModel):
    password: str

# Schema para resposta (incluindo todos os campos do modelo)
class Login(LoginBase):
    id: int
    createAt: datetime
    updateAt: Optional[datetime] = None # updateAt pode ser None no início

    class Config:
        orm_mode = True # Permite que o Pydantic leia dados de modelos ORM (SQLAlchemy)
        from_attributes = True # Alias para orm_mode em Pydantic V2+