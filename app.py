from flask import Flask
from models import db
from utils import parse_date
from routes.associados import associados_bp
from routes.contribuicoes import contribuicoes_bp
from routes.eventos import eventos_bp
from routes.participacoes import participacoes_bp
from routes.interacoes import interacoes_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sindicato_crm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

# Register Blueprints
app.register_blueprint(associados_bp,    url_prefix='/associados')
app.register_blueprint(contribuicoes_bp, url_prefix='/contribuicoes')
app.register_blueprint(eventos_bp,       url_prefix='/eventos')
app.register_blueprint(participacoes_bp, url_prefix='/participacoes')
app.register_blueprint(interacoes_bp,    url_prefix='/interacoes')

if __name__ == '__main__':
    app.run(debug=True)
