from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .associados import Associado
from .contribuicoes import Contribuicao
from .eventos import Evento
from .participacoes import Participacao
from .interacoes import Interacao
