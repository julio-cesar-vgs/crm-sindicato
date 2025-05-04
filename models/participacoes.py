from . import db

class Participacao(db.Model):
    __tablename__ = 'participacoes'
    id_participacao = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_evento = db.Column(db.Integer, db.ForeignKey('eventos.id_evento'), nullable=False)
    id_associado = db.Column(db.Integer, db.ForeignKey('associados.id_associado'), nullable=False)
    feedback = db.Column(db.String)

    def to_dict(self):
        return {
            'id_participacao': self.id_participacao,
            'id_evento': self.id_evento,
            'id_associado': self.id_associado,
            'feedback': self.feedback
        }
