from .associados import router as associados_router
from .contribuicoes import router as contribuicoes_router
from .eventos import router as eventos_router
from .interacoes import router as interacoes_router
from .participacoes import router as participacoes_router
from .login import router as login_router

__all__ = [
    "associados_router",
    "contribuicoes_router",
    "eventos_router",
    "interacoes_router",
    "participacoes_router",
    "login_router",
]
