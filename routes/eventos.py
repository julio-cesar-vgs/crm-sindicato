from flask import Blueprint, request, jsonify, abort
from models import db, Evento
from utils import parse_date

eventos_bp = Blueprint('eventos', __name__)

@eventos_bp.route('', methods=['GET'])
def list_eventos():
    return jsonify([e.to_dict() for e in Evento.query.all()])

@eventos_bp.route('/<int:id>', methods=['GET'])
def get_evento(id):
    e = Evento.query.get_or_404(id)
    return jsonify(e.to_dict())

@eventos_bp.route('', methods=['POST'])
def create_evento():
    data = request.get_json()
    try:
        e = Evento(
            nome_evento=data['nome_evento'],
           	data_evento=parse_date(data.get('data_evento')),
            local_evento=data.get('local_evento'),
            descricao=data.get('descricao')
        )
    except KeyError as e:
        abort(400, description=f'Atributo obrigatório faltando: {e.args[0]}')
    db.session.add(e)
    db.session.commit()
    return jsonify({'id_evento': e.id_evento}), 201

@eventos_bp.route('/<int:id>', methods=['PUT'])
def	update_evento(id):
    e = Evento.query.get_or_404(id)
    data = request.get_json()
    if 'nome_evento' in data:
        e.nome_evento = data['nome_evento']
    if 'data_evento' in data:
        e.data_evento = parse_date(data.get('data_evento'))
    if 'local_evento' in data:
        e.local_evento = data['local_evento']
    if 'descricao' in data:
        e.descricao = data['descricao']
    db.session.commit()
    return jsonify({'message': 'Evento atualizado.'})

@eventos_bp.route('/<int:id>', methods=['DELETE'])
def delete_evento(id):
    e = Evento.query.get_or_404(id)
    db.session.delete(e)
    db.session.commit()
    return jsonify({'message': 'Evento removido.'})
