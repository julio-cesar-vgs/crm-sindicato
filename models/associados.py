from . import db

class Associado(db.Model):
    __tablename__ = 'associados'
    id_associado = db.Column(db.Integer, primary_key=True, autoincrement=True)
    razao_social = db.Column(db.String, nullable=False)
    cnpj = db.Column(db.String, unique=True, nullable=False)
    contato = db.Column(db.String)
    ramo_atuacao = db.Column(db.String)
    cidade = db.Column(db.String)
    estado = db.Column(db.String)
    data_associacao = db.Column(db.Date)
    status_contribuicao = db.Column(db.String)

    contribuicoes = db.relationship('Contribuicao', backref='associado', lazy=True)
    participacoes = db.relationship('Participacao', backref='associado', lazy=True)
    interacoes = db.relationship('Interacao', backref='associado', lazy=True)

    def to_dict(self):
        return {
            'id_associado': self.id_associado,
            'razao_social': self.razao_social,
            'cnpj': self.cnpj,
            'contato': self.contato,
            'ramo_atuacao': self.ramo_atuacao,
            'cidade': self.cidade,
            'estado': self.estado,
            'data_associacao': self.data_associacao.isoformat() if self.data_associacao else None,
            'status_contribuicao': self.status_contribuicao
        }
