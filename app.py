import os
import sys

# Adicionar o diretório atual ao path para importações
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from utils.db import close_connection

app = Flask(__name__)

# Configurações
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'chave-super-secreta-parla')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600  # 1 hora

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Registrar fechamento de conexão do banco
app.teardown_appcontext(close_connection)

# Importar blueprints
try:
    from routes.auth_routes import auth_bp, blacklist
    from routes.atividade_routes import atividade_bp
    from routes.personagem_routes import personagem_bp
    from routes.post_routes import post_bp
    from routes.user_routes import user_bp
except ImportError as e:
    print(f"Erro ao importar blueprints: {e}")
    raise

@jwt.token_in_blocklist_loader
def verifica_token(jwt_header, jwt_payload):
    return jwt_payload['jti'] in blacklist

# Registro dos Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(atividade_bp, url_prefix='/atividade')
app.register_blueprint(personagem_bp, url_prefix='/personagem')
app.register_blueprint(post_bp, url_prefix='/post')
app.register_blueprint(user_bp, url_prefix='/user')

# Rota inicial
@app.route('/')
def index():
    return {'msg': 'API Parla com Autenticação JWT ativa!'}

@app.route('/health')
def health():
    return {'status': 'ok'}, 200

if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_ENV') != 'production'
    app.run(debug=debug_mode, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
