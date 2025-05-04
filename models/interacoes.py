from . import db

class Interacao(db.Model):
    __tablename__ = 'interacoes'
    id_interacao = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_associado = db.Column(db.Integer, db.ForeignKey('associados.id_associado'), nullable=False)
    tipo_interacao = db.Column(db.String, nullable=False)
    data_interacao = db.Column(db.Date, nullable=False)
    descricao = db.Column(db.String)

    def to_dict(self):
        return {
            'id_interacao': self.id_interacao,
            'id_associado': self.id_associado,
            'tipo_interacao': self.tipo_interacao,
            'data_interacao': self.data_interacao.isoformat() if self.data_interacao else None,
            'descricao': self.descricao
        }
