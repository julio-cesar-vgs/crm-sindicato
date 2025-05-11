from flask import Blueprint, request, jsonify, abort
from models import db, Associado
from utils import parse_date

associados_bp = Blueprint('associados', __name__)

@associados_bp.route('', methods=['GET'])
def list_associados():
    return jsonify([a.to_dict() for a in Associado.query.all()])

@associados_bp.route('/<int:id>', methods=['GET'])
def get_associado(id):
    a = Associado.query.get_or_404(id)
    return jsonify(a.to_dict())

@associados_bp.route('/count', methods=['GET'])
def count_associados():
    try:
        count = Associado.query.count()
        return jsonify({"count": count}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@associados_bp.route('', methods=['POST'])
def create_associado():
    data = request.get_json()
    try:
        assoc = Associado(
            razao_social=data['razao_social'],
            cnpj=data['cnpj'],
            contato=data.get('contato'),
            ramo_atuacao=data.get('ramo_atuacao'),
            cidade=data.get('cidade'),
            estado=data.get('estado'),
            data_associacao=parse_date(data.get('data_associacao')),
            status_contribuicao=data.get('status_contribuicao')
        )
    except KeyError as e:
        abort(400, description=f'Atributo obrigatório faltando: {e.args[0]}')
    db.session.add(assoc)
    db.session.commit()
    return jsonify({'id_associado': assoc.id_associado}), 201

@associados_bp.route('/<int:id>', methods=['PUT'])
def update_associado(id):
    a = Associado.query.get_or_404(id)
    data = request.get_json()
    for field in ['razao_social', 'cnpj', 'contato', 'ramo_atuacao', 'cidade', 'estado', 'status_contribuicao']:
        if field in data:
            setattr(a, field, data[field])
    if 'data_associacao' in data:
        a.data_associacao = parse_date(data.get('data_associacao'))
    db.session.commit()
    return jsonify({'message': 'Associado atualizado com sucesso.'})

@associados_bp.route('/<int:id>', methods=['DELETE'])
def delete_associado(id):
    a = Associado.query.get_or_404(id)
    db.session.delete(a)
    db.session.commit()
    return jsonify({'message': 'Associado removido.'})
