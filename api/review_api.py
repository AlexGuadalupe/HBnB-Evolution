from flask import Flask, request, jsonify
from datetime import datetime
import uuid
from persistence.DataManager import DataManager

app = Flask(__name__)

# Initialize DataManager
data = DataManager()

# Review data model
class Review:
    def __init__(self, place_id, user_id, rating, comment):
        self.review_id = uuid.uuid4()  # Generate a unique ID
        self.place_id = place_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment
        self.created_at = datetime.now()
        self.updated_at = self.created_at

# Endpoint to create a review
@app.route('/places/<int:place_id>/reviews', methods=['POST'])
def create_review(place_id):
    if request.method == 'POST':
        data = request.get_json()
        if 'user_id' in data and 'rating' in data and 'comment' in data:
            user_id = data['user_id']
            rating = data['rating']
            comment = data['comment']
            review = data.create_review(place_id, user_id, rating, comment)
            return jsonify({'message': 'Review created successfully', 'review_id': str(review.review_id)}), 201
        else:
            return jsonify({'error': 'Invalid input'}), 400

# Endpoint to retrieve all reviews for a place
@app.route('/places/<int:place_id>/reviews', methods=['GET'])
def get_reviews(place_id):
    if request.method == 'GET':
        place_reviews = data.get_reviews(place_id)
        return jsonify([review.__dict__ for review in place_reviews]), 200

# Endpoint to retrieve a specific review
@app.route('/places/<int:place_id>/reviews/<uuid:review_id>', methods=['GET'])  # Use UUID for review_id
def get_review(place_id, review_id):
    if request.method == 'GET':
        review = data.get_review(place_id, review_id)
        if review:
            return jsonify(review.__dict__), 200
        else:
            return jsonify({'error': 'Review not found'}), 404

# Endpoint to update a review
@app.route('/places/<int:place_id>/reviews/<uuid:review_id>', methods=['PUT'])
def update_review(place_id, review_id):
    if request.method == 'PUT':
        data = request.get_json()
        result = data.update_review(place_id, review_id, data)
        return jsonify(result), 200

# Endpoint to delete a review
@app.route('/places/<int:place_id>/reviews/<uuid:review_id>', methods=['DELETE'])
def delete_review(place_id, review_id):
    if request.method == 'DELETE':
        result = data.delete_review(place_id, review_id)
        return jsonify(result), 200

# User endpoints - Example:

@app.route('/users', methods=['POST'])
def create_user():
    if request.method == 'POST':
        user_data = request.get_json()
        # Assuming user_data contains the required fields (e.g., username, email)
        user = data.create_user(user_data)  # Use the DataManager to create the user
        return jsonify({'message': 'User created successfully', 'user_id': user.user_id}), 201
    else:
        return jsonify({'error': 'Invalid request'}), 400

@app.route('/users', methods=['GET'])
def get_users():
    if request.method == 'GET':
        users = data.get_users()
        return jsonify([user.__dict__ for user in users]), 200
    else:
        return jsonify({'error': 'Invalid request'}), 400

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if request.method == 'GET':
        user = data.get_user(user_id)
        if user:
            return jsonify(user.__dict__), 200
        else:
            return jsonify({'error': 'User not found'}), 404
    else:
        return jsonify({'error': 'Invalid request'}), 400

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if request.method == 'PUT':
        user_data = request.get_json()
        result = data.update_user(user_id, user_data)
        if result:
            return jsonify({'message': 'User updated successfully'}), 200
        else:
            return jsonify({'error': 'User not found'}), 404
    else:
        return jsonify({'error': 'Invalid request'}), 400

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if request.method == 'DELETE':
        result = data.delete_user(user_id)
        if result:
            return jsonify({'message': 'User deleted successfully'}), 200
        else:
            return jsonify({'error': 'User not found'}), 404
    else:
        return jsonify({'error': 'Invalid request'}), 400


if __name__ == '__main__':
    app.run(debug=True)
