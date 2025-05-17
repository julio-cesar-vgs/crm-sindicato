from sqlalchemy import Column, Integer, String, Date, ForeignKey
from database import Base

class Interacao(Base):
    __tablename__ = 'interacoes'
    id_interacao = Column(Integer, primary_key=True, autoincrement=True)
    id_associado = Column(Integer, ForeignKey('associados.id_associado'), nullable=False)
    tipo_interacao = Column(String, nullable=False)
    data_interacao = Column(Date, nullable=False)
    descricao = Column(String)
