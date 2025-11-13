from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.personagem_service import (
    add_personagem, get_personagem, get_personagens,
    edit_personagem, remove_personagem
)

personagem_bp = Blueprint('personagem_bp', __name__)

@personagem_bp.route('/personagens', methods=['POST'])
@jwt_required()
def criar_personagem():
    current_user_id = get_jwt_identity()
    data = request.get_json()
    id = add_personagem(
        current_user_id,  # usando o ID do usuário autenticado
        data.get('sapato'),
        data.get('acessorios'),
        data.get('roupa'),
        data.get('cabelo'),
        data.get('corpo')
    )
    return jsonify({'id': id}), 201

@personagem_bp.route('/personagens', methods=['GET'])
@jwt_required()
def listar_personagens():
    current_user_id = get_jwt_identity()
    personagens = get_personagens()
    return jsonify(personagens), 200

@personagem_bp.route('/personagens/<int:personagem_id>', methods=['GET'])
@jwt_required()
def buscar_personagem(personagem_id):
    current_user_id = get_jwt_identity()
    personagem = get_personagem(personagem_id)
    if personagem:
        return jsonify(personagem), 200
    return jsonify({'erro': 'Personagem não encontrado'}), 404

@personagem_bp.route('/personagens/<int:personagem_id>', methods=['PUT'])
def atualizar_personagem(personagem_id):
    data = request.get_json()
    edit_personagem(
        personagem_id,
        data.get('sapato'),
        data.get('acessorios'),
        data.get('roupa'),
        data.get('cabelo'),
        data.get('corpo')
    )
    return jsonify({'msg': 'Personagem atualizado'}), 200

@personagem_bp.route('/personagens/<int:personagem_id>', methods=['DELETE'])
def deletar_personagem(personagem_id):
    remove_personagem(personagem_id)
    return jsonify({'msg': 'Personagem deletado'}), 200
