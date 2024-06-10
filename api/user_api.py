from flask import Flask, request, jsonify
from persistence.DataManager import DataManager

app = Flask(__name__)

data = DataManager()


@app.route('/users', methods=['POST'])
def create_user():


@app.route('/users', methods=['GET'])
def get_users():
    """Obtiene una lista de todos los usuarios."""


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Obtiene detalles de un usuario específico."""


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Actualiza un usuario existente."""


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Elimina un usuario."""


if __name__ == '__main__':
    app.run(debug=True)
