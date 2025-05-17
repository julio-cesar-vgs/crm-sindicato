from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

from .associados import Associado
from .contribuicoes import Contribuicao
from .eventos import Evento
from .participacoes import Participacao
from .interacoes import Interacao
from .login import Login
