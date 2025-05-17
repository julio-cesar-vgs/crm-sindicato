from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from database import Base

class Evento(Base):
    __tablename__ = 'eventos'
    id_evento = Column(Integer, primary_key=True, autoincrement=True)
    nome_evento = Column(String, nullable=False)
    data_evento = Column(Date, nullable=False)
    local_evento = Column(String)
    descricao = Column(String)

    participacoes = relationship('Participacao', backref='evento', lazy=True)
