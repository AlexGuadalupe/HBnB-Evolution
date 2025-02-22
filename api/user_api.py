from flask import Flask, abort, Blueprint, request, jsonify
from persistence.DataManager import DataManager
from datetime import datetime

user_blueprint = Blueprint('user_api', __name__)

data = DataManager()

users = []

@user_blueprint.route('/users', methods=['POST'])
def create_user():
    """Crear un nuevo usuario."""
    if not request.json or not 'email' in request.json or not 'password' in request.json:
        abort(400, description="Missing required fields")

    email = request.json['email']
    password = request.json['password']
    first_name = request.json.get('first_name', '')
    last_name = request.json.get('last_name', '')

    if '@' not in email:  # Simple email validation
        abort(400, description="Invalid email format")

    if data.get_user_by_email(email):
        abort(409, description="Email already exists")

    user = {
        'user_id' : len('user_id') + 1,
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'created_at': datetime.now(),
        'updated_at': datetime.now()
    }
    new_user = data.create_user(user)
    return jsonify(new_user), 201


@user_blueprint.route('/users', methods=['GET'])
def get_all_users():
    """Obtiene una lista de todos los usuarios."""
    return jsonify(users), 200


@user_blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Obtiene detalles de un usuario específico."""
    user = data.get_user_by_id(user_id)
    if not user:
        abort(404, description="User not found")
    return jsonify(user), 200


@user_blueprint.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Actualiza un usuario existente."""
    user = data.get_user_by_id(user_id)
    if not user:
        abort(404, description="User not found")

    data_json = request.get_json()
    email = data_json.get('email', user['email'])
    first_name = data_json.get('first_name', user['first_name'])
    last_name = data_json.get('last_name', user['last_name'])

    if not email or not first_name or not last_name:
        abort(400, description="Missing required fields")

    if '@' not in email:  # Simple email validation
        abort(400, description="Invalid email format")

    if email != user['email'] and data.get_user_by_email(email):
        abort(409, description="Email already exists")

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
        abort(404, description="User not found")
    data.delete_user(user_id)
    return '', 204
