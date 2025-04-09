# setup_crm.py
app_py = '''from flask import Flask, jsonify, request
import database

app = Flask(__name__)
database.criar_tabelas()

@app.route("/")
def index():
    return "CRM do Sindicato rodando com Flask + SQLite!"

@app.route("/associados", methods=["GET"])
def listar_associados():
    con = database.conectar_banco()
    cur = con.cursor()
    cur.execute("SELECT * FROM associados")
    associados = cur.fetchall()
    con.close()
    return jsonify(associados)

if __name__ == "__main__":
    app.run(debug=True)
'''

database_py = '''import sqlite3

def conectar_banco():
    return sqlite3.connect("sindicato_crm.db")

def criar_tabelas():
    con = conectar_banco()
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS associados (
            id_associado INTEGER PRIMARY KEY AUTOINCREMENT,
            razao_social TEXT NOT NULL,
            cnpj TEXT UNIQUE,
            contato TEXT,
            ramo_atuacao TEXT,
            cidade TEXT,
            estado TEXT,
            data_associacao DATE,
            status_contribuicao TEXT,
            ativo BOOLEAN DEFAULT 1
        );
    """)
    con.commit()
    con.close()
'''

with open("app.py", "w") as f:
    f.write(app_py)

with open("database.py", "w") as f:
    f.write(database_py)

print("Arquivos app.py e database.py criados com sucesso!")
