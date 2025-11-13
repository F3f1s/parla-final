from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt, JWTManager
from datetime import timedelta
from utils.db import get_db
from models.user import User

auth_bp = Blueprint('auth', __name__)
bcrypt = Bcrypt()

# Lista negra para tokens inválidos
blacklist = set()

@auth_bp.record
def record_params(setup_state):
    app = setup_state.app
    bcrypt.init_app(app)

# Função auxiliar: verificar se o token está na blacklist
@auth_bp.before_app_request
def check_if_token_in_blacklist():
    from flask import request
    if request.endpoint and "static" not in request.endpoint:
        jwt_data = get_jwt()
        if jwt_data and jwt_data["jti"] in blacklist:
            return jsonify({"msg": "Token inválido. Faça login novamente."}), 401

# Registro de novo usuário
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')
    senha = data.get('senha')

    if not nome or not email or not senha:
        return jsonify({'erro': 'Campos obrigatórios ausentes.'}), 400

    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM user WHERE email = ?", (email,))
    if cursor.fetchone():
        return jsonify({'erro': 'Usuário já existe.'}), 409

    senha_hash = bcrypt.generate_password_hash(senha).decode('utf-8')
    cursor.execute("INSERT INTO user (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha_hash))
    db.commit()

    return jsonify({'msg': 'Usuário registrado com sucesso!'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    senha = data.get('senha')

    if not email or not senha:
        return jsonify({'erro': 'Email e senha são obrigatórios.'}), 400

    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM user WHERE email = ?", (email,))
    user = cursor.fetchone()

    if user and bcrypt.check_password_hash(user[3], senha):  # assumindo que a senha está na coluna 3
        access_token = create_access_token(identity=user[0])  # user[0] é o ID do usuário
        return jsonify({'access_token': access_token}), 200
    
    return jsonify({'erro': 'Credenciais inválidas.'}), 401

@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    blacklist.add(jti)
    return jsonify({'msg': 'Logout realizado com sucesso!'}), 200


# Login e geração do token JWT
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    senha = data.get('senha')

    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM user WHERE email = ?", (email,))
    user = cursor.fetchone()

    if not user or not bcrypt.check_password_hash(user['senha'], senha):
        return jsonify({'erro': 'Credenciais inválidas.'}), 401

    token = create_access_token(identity=user['email'], expires_delta=timedelta(hours=1))
    return jsonify({'token': token, 'msg': 'Login bem-sucedido!'}), 200


# Logout e invalidação do token
@auth_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]
    blacklist.add(jti)
    return jsonify({"msg": "Logout realizado com sucesso!"}), 200


# Rota de teste protegida
@auth_bp.route('/perfil', methods=['GET'])
@jwt_required()
def perfil():
    usuario = get_jwt_identity()
    return jsonify({'msg': f'Bem-vindo, {usuario}!'}), 200
