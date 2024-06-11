from flask import Blueprint, request, jsonify
from persistence.DataManager import DataManager
from datetime import datetime

user_blueprint = Blueprint('user_api', __name__)

users_db = {}


@user_blueprint.route('/users', methods=['POST'])
def create_user():
    """Crear un nuevo usuario."""
    data_json = request.get_json()
    email = data_json.get('email')
    first_name = data_json.get('first_name')
    last_name = data_json.get('last_name')

    if not email or not first_name or not last_name:
        return jsonify({'error': 'Missing required fields'}), 400

    if '@' not in email:  # Simple email validation
        return jsonify({'error': 'Invalid email format'}), 400

    if data.get_user_by_email(email):
        return jsonify({'error': 'Email already exists'}), 409

    user = {
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'created_at': datetime.utcnow(),
        'updated_at': datetime.utcnow()
    }
    new_user = data.create_user(user)
    return jsonify(new_user), 201


@user_blueprint.route('/users', methods=['GET'])
def get_users():
    """Obtiene una lista de todos los usuarios."""
    users = data.get_all_users()
    return jsonify(users), 200


@user_blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Obtiene detalles de un usuario específico."""
    user = data.get_user_by_id(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user), 200


@user_blueprint.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Actualiza un usuario existente."""
    user = data.get_user_by_id(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data_json = request.get_json()
    email = data_json.get('email', user['email'])
    first_name = data_json.get('first_name', user['first_name'])
    last_name = data_json.get('last_name', user['last_name'])

    if not email or not first_name or not last_name:
        return jsonify({'error': 'Missing required fields'}), 400

    if '@' not in email:  # Simple email validation
        return jsonify({'error': 'Invalid email format'}), 400

    if email != user['email'] and data.get_user_by_email(email):
        return jsonify({'error': 'Email already exists'}), 409

    updated_user = {
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'updated_at': datetime.utcnow()
    }
    updated_user = data.update_user(user_id, updated_user)
    return jsonify(updated_user), 200


@user_blueprint.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Elimina un usuario."""
    user = data.get_user_by_id(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    data.delete_user(user_id)
    return '', 204
