from flask import request, jsonify, Blueprint
from datetime import datetime
from persistence.DataManager import DataManager

review_blueprint = Blueprint('review_api', __name__)

# Initialize DataManager
data = DataManager() 

@review_blueprint.route('/places/<int:place_id>/reviews', methods=['POST'])
@login_required
def create_review(place_id):
    if request.method == 'POST':
        data_request = request.get_json()
        if 'rating' in data_request and 'comment' in data_request:
            rating = data_request['rating']
            comment = data_request['comment']
            # Use DataManager to create the review
            review_id = data.create_review(place_id, current_user.id, rating, comment)
            return jsonify({'message': 'Review created successfully', 'review_id': str(review_id)}), 201
        else:
            return jsonify({'error': 'Invalid input'}), 400

@review_blueprint.route('/places/<int:place_id>/reviews', methods=['GET'])
def get_reviews(place_id):
    if request.method == 'GET':
        # Use DataManager to retrieve reviews
        place_reviews = data.get_reviews(place_id)
        return jsonify([review.__dict__ for review in place_reviews]), 200

@review_blueprint.route('/places/<int:place_id>/reviews/<uuid:review_id>', methods=['GET'])
def get_review(place_id, review_id):
    if request.method == 'GET':
        # Use DataManager to retrieve a specific review
        review = data.get_review(place_id, review_id)
        if review:
            return jsonify(review.__dict__), 200
        else:
            return jsonify({'error': 'Review not found'}), 404

@review_blueprint.route('/places/<int:place_id>/reviews/<uuid:review_id>', methods=['PUT'])
@login_required
def update_review(place_id, review_id):
    if request.method == 'PUT':
        # Use DataManager to get the review
        review = data.get_review(place_id, review_id)
        if review and review.user_id == current_user.id:
            data_request = request.get_json()
            if 'rating' in data_request and 'comment' in data_request:
                rating = data_request['rating']
                comment = data_request['comment']
                # Use DataManager to update the review
                result = data.update_review(place_id, review_id, rating, comment)
                return jsonify(result), 200
            else:
                return jsonify({'error': 'Invalid input'}), 400
        else:
            return jsonify({'error': 'Unauthorized'}), 401

@review_blueprint.route('/places/<int:place_id>/reviews/<uuid:review_id>', methods=['DELETE'])
@login_required
def delete_review(place_id, review_id):
    if request.method == 'DELETE':
        # Use DataManager to get the review
        review = data.get_review(place_id, review_id)
        if review and review.user_id == current_user.id:
            # Use DataManager to delete the review
            result = data.delete_review(place_id, review_id)
            return jsonify(result), 200
        else:
            return jsonify({'error': 'Unauthorized'}), 401
