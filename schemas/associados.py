from pydantic import BaseModel
from typing import Optional
from datetime import date

class AssociadoBase(BaseModel):
    razao_social: str
    cnpj: str
    contato: Optional[str] = None
    ramo_atuacao: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None
    data_associacao: Optional[date] = None
    status_contribuicao: Optional[str] = None

class AssociadoCreate(AssociadoBase):
    pass

class AssociadoUpdate(AssociadoBase):
    razao_social: Optional[str] = None
    cnpj: Optional[str] = None
    contato: Optional[str] = None
    ramo_atuacao: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None
    data_associacao: Optional[date] = None
    status_contribuicao: Optional[str] = None


class AssociadoResponse(AssociadoBase):
    id_associado: int

    class Config:
        orm_mode = True