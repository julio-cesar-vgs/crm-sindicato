from flask import Blueprint, request, jsonify
import database

associados_bp = Blueprint('associados', __name__)

@associados_bp.route("/associados", methods=["GET"])
def listar_associados():
    con = database.conectar_banco()
    cur = con.cursor()
    cur.execute("SELECT * FROM associados")
    associados = cur.fetchall()
    con.close()

    resultado = []
    for row in associados:
        resultado.append({
            "id": row[0],
            "razao_social": row[1],
            "cnpj": row[2],
            "contato": row[3],
            "ramo_atuacao": row[4],
            "cidade": row[5],
            "estado": row[6],
            "data_associacao": row[7],
            "status_contribuicao": row[8],
            "ativo": bool(row[9])
        })
    return jsonify(resultado)

@associados_bp.route("/associados", methods=["POST"])
def cadastrar_associado():
    data = request.json
    try:
        con = database.conectar_banco()
        cur = con.cursor()
        cur.execute("""
            INSERT INTO associados 
            (razao_social, cnpj, contato, ramo_atuacao, cidade, estado, data_associacao, status_contribuicao)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data["razao_social"],
            data["cnpj"],
            data.get("contato"),
            data.get("ramo_atuacao"),
            data.get("cidade"),
            data.get("estado"),
            data.get("data_associacao"),
            data["status_contribuicao"]
        ))
        con.commit()
        return jsonify({"mensagem": "Associado cadastrado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 400
    finally:
        con.close()
