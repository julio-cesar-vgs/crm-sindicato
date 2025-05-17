from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from database import Base

class Associado(Base):
    __tablename__ = 'associados'
    id_associado = Column(Integer, primary_key=True, autoincrement=True)
    razao_social = Column(String, nullable=False)
    cnpj = Column(String, unique=True, nullable=False)
    contato = Column(String)
    ramo_atuacao = Column(String)
    cidade = Column(String)
    estado = Column(String)
    data_associacao = Column(Date)
    status_contribuicao = Column(String)

    contribuicoes = relationship('Contribuicao', backref='associado', lazy=True)
    participacoes = relationship('Participacao', backref='associado', lazy=True)
    interacoes = relationship('Interacao', backref='associado', lazy=True)
