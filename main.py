from fastapi import FastAPI
from routes import associados_router, contribuicoes_router, eventos_router, interacoes_router, participacoes_router, login_router
from database import engine, Base

# Opcional: Cria as tabelas no banco de dados se elas não existirem
# Remova ou comente esta parte se você gerencia o banco de dados de outra forma (ex: Alembic)
try:
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas (se não existiam).")
except Exception as e:
    print(f"Erro ao criar tabelas: {e}")


app = FastAPI(
    title="Nome da sua API",  # <--- Customize o título
    description="Descrição da sua API", # <--- Customize a descrição
    version="1.0.0",
    docs_url="/docs",       # URL para a Swagger UI (padrão)
    redoc_url="/redoc"      # Opcional: URL para a ReDoc (padrão)
)

# Inclui todos os seus routers na aplicação principal
app.include_router(associados_router, prefix="/associados", tags=["Associados"])
app.include_router(contribuicoes_router, prefix="/contribuicoes", tags=["Contribuicoes"])
app.include_router(eventos_router, prefix="/eventos", tags=["Eventos"])
app.include_router(interacoes_router, prefix="/interacoes", tags=["Interacoes"])
app.include_router(participacoes_router, prefix="/participacoes", tags=["Participacoes"])
app.include_router(login_router, prefix="/login", tags=["Login"])

@app.get("/")
def read_root():
    return {"message": "API está funcionando!"}
