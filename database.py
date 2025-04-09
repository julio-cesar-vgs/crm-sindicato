import sqlite3

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
