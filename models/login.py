from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from . import Base

class Login(Base):
    __tablename__ = 'login'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    createAt = Column(DateTime, server_default=func.now())
    updateAt = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return f"<Login(id={self.id}, nome='{self.nome}')>"