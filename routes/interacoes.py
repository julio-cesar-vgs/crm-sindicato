from flask import Blueprint, request, jsonify, abort
from models import db, Interacao
from utils import parse_date

interacoes_bp = Blueprint('interacoes', __name__)

@interacoes_bp.route('', methods=['GET'])
def list_interacoes():
    return jsonify([i.to_dict() for i in Interacao.query.all()])

@interacoes_bp.route('', methods=['POST'])
def create_interacao():
    data = request.get_json()
    try:
        i = Interacao(
            id_associado=data['id_associado'],
            tipo_interacao=data['tipo_interacao'],
            data_interacao=parse_date(data.get('data_interacao')),
            descricao=data.get('descricao')
        )
    except KeyError as e:
        abort(400, description=f'Atributo obrigatório faltando: {e.args[0]}')
    db.session.add(i)
    db.session.commit()
    return jsonify({'id_interacao': i.id_interacao}), 201
