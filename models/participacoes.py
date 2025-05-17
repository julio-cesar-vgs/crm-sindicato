from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Participacao(Base):
    __tablename__ = 'participacoes'
    id_participacao = Column(Integer, primary_key=True, autoincrement=True)
    id_evento = Column(Integer, ForeignKey('eventos.id_evento'), nullable=False)
    id_associado = Column(Integer, ForeignKey('associados.id_associado'), nullable=False)
    feedback = Column(String)
