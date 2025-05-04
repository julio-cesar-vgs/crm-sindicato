from . import db

class Evento(db.Model):
    __tablename__ = 'eventos'
    id_evento = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_evento = db.Column(db.String, nullable=False)
    data_evento = db.Column(db.Date, nullable=False)
    local_evento = db.Column(db.String)
    descricao = db.Column(db.String)

    participacoes = db.relationship('Participacao', backref='evento', lazy=True)

    def to_dict(self):
        return {
            'id_evento': self.id_evento,
            'nome_evento': self.nome_evento,
            'data_evento': self.data_evento.isoformat() if self.data_evento else None,
            'local_evento': self.local_evento,
            'descricao': self.descricao
        }
