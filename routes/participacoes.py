from flask import Blueprint, request, jsonify, abort
from models import db, Participacao

participacoes_bp = Blueprint('participacoes', __name__)

@participacoes_bp.route('', methods=['GET'])
def list_participacoes():
    return jsonify([p.to_dict() for p in Participacao.query.all()])

@participacoes_bp.route('', methods=['POST'])
def create_participacao():
    data = request.get_json()
    try:
        p = Participacao(
            id_evento=data['id_evento'],
            id_associado=data['id_associado'],
            feedback=data.get('feedback')
        )
    except KeyError as e:
        abort(400, description=f'Atributo obrigatório faltando: {e.args[0]}')
    db.session.add(p)
    db.session.commit()
    return jsonify({'id_participacao': p.id_participacao}), 201
