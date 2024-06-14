from flask import request, jsonify, Blueprint
from datetime import datetime
from persistence.DataManager import DataManager
from flask_login import current_user, login_required

review_blueprint = Blueprint('review_api', __name__)

data = DataManager()

class Review:
    def __init__(self, place_id, user_id, rating, comment):
        self.place_id = place_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment
        self.created_at = datetime.now()
        self.updated_at = self.created_at

# Endpoint to create a review
@review_blueprint.route('/places/<int:place_id>/reviews', methods=['POST'])
@login_required
def create_review(place_id):
    if request.method == 'POST':
        data_request = request.get_json()
        if 'rating' in data_request and 'comment' in data_request:
            rating = data_request['rating']
            comment = data_request['comment']
            review = Review(place_id, current_user.id, rating, comment)
            data.create_review(review)
            return jsonify({'message': 'Review created successfully', 'review_id': str(review.review_id)}), 201
        else:
            return jsonify({'error': 'Invalid input'}), 400

# Endpoint to retrieve all reviews for a place
@review_blueprint.route('/places/<int:place_id>/reviews', methods=['GET'])
def get_reviews(place_id):
    if request.method == 'GET':
        place_reviews = data.get_reviews(place_id)
        return jsonify([review.__dict__ for review in place_reviews]), 200

# Endpoint to retrieve a specific review
@review_blueprint.route('/places/<int:place_id>/reviews/<uuid:review_id>', methods=['GET'])
def get_review(place_id, review_id):
    if request.method == 'GET':
        review = data.get_review(place_id, review_id)
        if review:
            return jsonify(review.__dict__), 200
        else:
            return jsonify({'error': 'Review not found'}), 404

# Endpoint to update a review
@review_blueprint.route('/places/<int:place_id>/reviews/<uuid:review_id>', methods=['PUT'])
@login_required
def update_review(place_id, review_id):
    if request.method == 'PUT':
        review = data.get_review(place_id, review_id)
        if review and review.user_id == current_user.id:
            data_request = request.get_json()
            if 'rating' in data_request and 'comment' in data_request:
                rating = data_request['rating']
                comment = data_request['comment']
                result = data.update_review(place_id, review_id, rating, comment)
                return jsonify(result), 200
            else:
                return jsonify({'error': 'Invalid input'}), 400
        else:
            return jsonify({'error': 'Unauthorized'}), 401

# Endpoint to delete a review
@review_blueprint.route('/places/<int:place_id>/reviews/<uuid:review_id>', methods=['DELETE'])
@login_required
def delete_review(place_id, review_id):
    if request.method == 'DELETE':
        review = data.get_review(place_id, review_id)
        if review and review.user_id == current_user.id:
            result = data.delete_review(place_id, review_id)
            return jsonify(result), 200
        else:
            return jsonify({'error': 'Unauthorized'}), 401
