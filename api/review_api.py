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
        data_request = request.get_json()
        if 'user_id' in data_request and 'rating' in data_request and 'comment' in data_request:
            user_id = data_request['user_id']
            rating = data_request['rating']
            comment = data_request['comment']
            review = Review(place_id, user_id, rating, comment)
            data.create_review(review)
            return jsonify({'message': 'Review created successfully', 'eview_id': str(review.review_id)}), 201
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
        data_request = request.get_json()
        if 'rating' in data_request and 'comment' in data_request:
            rating = data_request['rating']
            comment = data_request['comment']
            result = data.update_review(place_id, review_id, rating, comment)
            return jsonify(result), 200
        else:
            return jsonify({'error': 'Invalid input'}), 400

# Endpoint to delete a review
@app.route('/places/<int:place_id>/reviews/<uuid:review_id>', methods=['DELETE'])
def delete_review(place_id, review_id):
    if request.method == 'DELETE':
        result = data.delete_review(place_id, review_id)
        return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
