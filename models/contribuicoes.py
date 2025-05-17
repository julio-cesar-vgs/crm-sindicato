from sqlalchemy import Column, Integer, Numeric, String, Date, ForeignKey
from database import Base

class Contribuicao(Base):
    __tablename__ = 'contribuicoes'
    id_contribuicao = Column(Integer, primary_key=True, autoincrement=True)
    id_associado = Column(Integer, ForeignKey('associados.id_associado'), nullable=False)
    valor = Column(Numeric, nullable=False)
    data_pagamento = Column(Date)
    status_pagamento = Column(String)
