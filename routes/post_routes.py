from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from dao.post_dao import (
    create_post, get_post_by_id, get_posts_by_user,
    get_all_posts, update_post, delete_post
)

# Define o blueprint para as rotas de posts
# Agrupa todas as rotas relacionadas a posts sob o prefixo 'post_bp'
post_bp = Blueprint('post_bp', __name__)

@post_bp.route('/posts', methods=['POST'])
@jwt_required()
def criar_post():
    current_user_id = get_jwt_identity()
    data = request.get_json()
    post_id = create_post(
        current_user_id,  # usando o ID do usuário autenticado
        data.get('title'),
        data.get('content')
    )
    return jsonify({'id': post_id}), 201

@post_bp.route('/posts', methods=['GET'])
@jwt_required()
def listar_posts():
    current_user_id = get_jwt_identity()
    posts = get_all_posts()
    return jsonify(posts), 200

@post_bp.route('/posts/<int:post_id>', methods=['GET'])
@jwt_required()
def get_post(post_id):
    current_user_id = get_jwt_identity()
    post = get_post_by_id(post_id)
    if post:
        return jsonify(post), 200
    return jsonify({'erro': 'Post não encontrado'}), 404

@post_bp.route('/posts', methods=['GET'])
def listar_posts():
    posts = get_all_posts()
    return jsonify(posts), 200

@post_bp.route('/posts/<int:post_id>', methods=['GET'])
def buscar_post(post_id):
    post = get_post_by_id(post_id)
    if post:
        return jsonify(post), 200
    return jsonify({'erro': 'Post não encontrado'}), 404

@post_bp.route('/posts/user/<int:user_id>', methods=['GET'])
def listar_posts_usuario(user_id):
    posts = get_posts_by_user(user_id)
    return jsonify(posts), 200

@post_bp.route('/posts/<int:post_id>', methods=['PUT'])
def atualizar_post(post_id):
    data = request.get_json()
    update_post(
        post_id,
        data.get('title'),
        data.get('content')
    )
    return jsonify({'msg': 'Post atualizado'}), 200

@post_bp.route('/posts/<int:post_id>', methods=['DELETE'])
def deletar_post(post_id):
    delete_post(post_id)
    return jsonify({'msg': 'Post deletado'}), 200