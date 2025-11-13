from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.atividade_service import (
    add_atividade, get_atividade, get_atividades,
    edit_atividade, remove_atividade
)

atividade_bp = Blueprint('atividade_bp', __name__)

@atividade_bp.route('/atividades', methods=['POST'])
@jwt_required()
def criar_atividade():
    current_user_id = get_jwt_identity()
    data = request.get_json()
    id = add_atividade(
        data.get('tentativas'),
        data.get('dificuldade'),
        data.get('horario'),
        data.get('erros')
    )
    return jsonify({'id': id}), 201

@atividade_bp.route('/atividades', methods=['GET'])
@jwt_required()
def listar_atividades():
    current_user_id = get_jwt_identity()
    atividades = get_atividades()
    return jsonify(atividades), 200

@atividade_bp.route('/atividades/<int:atividade_id>', methods=['GET'])
@jwt_required()
def buscar_atividade(atividade_id):
    current_user_id = get_jwt_identity()
    atividade = get_atividade(atividade_id)
    if atividade:
        return jsonify(atividade), 200
    return jsonify({'erro': 'Atividade não encontrada'}), 404

@atividade_bp.route('/atividades/<int:atividade_id>', methods=['PUT'])
def atualizar_atividade(atividade_id):
    data = request.get_json()
    edit_atividade(
        atividade_id,
        data.get('tentativas'),
        data.get('dificuldade'),
        data.get('horario'),
        data.get('erros')
    )
    return jsonify({'msg': 'Atividade atualizada'}), 200

@atividade_bp.route('/atividades/<int:atividade_id>', methods=['DELETE'])
def deletar_atividade(atividade_id):
    remove_atividade(atividade_id)
    return jsonify({'msg': 'Atividade deletada'}), 200
