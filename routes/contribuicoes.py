from flask import Blueprint, request, jsonify, abort
from models import db, Contribuicao
from utils import parse_date

contribuicoes_bp = Blueprint('contribuicoes', __name__)

@contribuicoes_bp.route('', methods=['GET'])
def list_contribuicoes():
    return jsonify([c.to_dict() for c in Contribuicao.query.all()])

@contribuicoes_bp.route('/<int:id>', methods=['GET'])
def get_contrib(id):
    c = Contribuicao.query.get_or_404(id)
    return jsonify(c.to_dict())

@contribuicoes_bp.route('', methods=['POST'])
def create_contrib():
    data = request.get_json()
    try:
        c = Contribuicao(
            id_associado=data['id_associado'],
            valor=data['valor'],
            data_pagamento=parse_date(data.get('data_pagamento')),
            status_pagamento=data.get('status_pagamento')
        )
    except KeyError as e:
        abort(400, description=f'Atributo obrigatório faltando: {e.args[0]}')
    db.session.add(c)
    db.session.commit()
    return jsonify({'id_contribuicao': c.id_contribuicao}), 201

@contribuicoes_bp.route('/<int:id>', methods=['PUT'])
def update_contrib(id):
    c = Contribuicao.query.get_or_404(id)
    data = request.get_json()
    if 'id_associado' in data:
        c.id_associado = data['id_associado']
    if 'valor' in data:
        c.valor = data['valor']
    if 'data_pagamento' in data:
        c.data_pagamento = parse_date(data.get('data_pagamento'))
    if 'status_pagamento' in data:
        c.status_pagamento = data['status_pagamento']
    db.session.commit()
    return jsonify({'message': 'Contribuição atualizada.'})

@contribuicoes_bp.route('/<int:id>', methods=['DELETE'])
def delete_contrib(id):
    c = Contribuicao.query.get_or_404(id)
    db.session.delete(c)
    db.session.commit()
    return jsonify({'message': 'Contribuição removida.'})
