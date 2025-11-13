from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.user_service import add_user, get_user

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['POST'])
@jwt_required()
def create():
    # Extract user data from request
    user_data = request.get_json()
    current_user_id = get_jwt_identity()
    
    # Call add_user from user_service
    response = add_user(user_data)
    
    # Return response as JSON
    return jsonify(response), 201

@user_bp.route('/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get(user_id):
    current_user_id = get_jwt_identity()
    # Call get_user from user_service
    response = get_user(user_id)
    
    # Return response as JSON
    return jsonify(response), 200

@user_bp.route('/me', methods=['GET'])
@jwt_required()
def get_my_info():
    current_user_id = get_jwt_identity()
    response = get_user(current_user_id)
    return jsonify(response), 200