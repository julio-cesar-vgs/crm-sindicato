from flask import Flask
import database
from routes.associados import associados_bp

app = Flask(__name__)
database.criar_tabelas()

# Registrar blueprint
app.register_blueprint(associados_bp)

@app.route("/")
def home():
    return "CRM do Sindicato rodando com Flask + SQLite!"

if __name__ == "__main__":
    app.run(debug=True)
