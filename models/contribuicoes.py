from . import db

class Contribuicao(db.Model):
    __tablename__ = 'contribuicoes'
    id_contribuicao = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_associado = db.Column(db.Integer, db.ForeignKey('associados.id_associado'), nullable=False)
    valor = db.Column(db.Numeric, nullable=False)
    data_pagamento = db.Column(db.Date)
    status_pagamento = db.Column(db.String)

    def to_dict(self):
        return {
            'id_contribuicao': self.id_contribuicao,
            'id_associado': self.id_associado,
            'valor': float(self.valor),
            'data_pagamento': self.data_pagamento.isoformat() if self.data_pagamento else None,
            'status_pagamento': self.status_pagamento
        }
