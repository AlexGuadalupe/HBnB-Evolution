from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

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

# In-memory list to store Review objects
reviews = []

# Endpoint to create a review
@app.route('/places/<int:place_id>/reviews', methods=['POST'])
def create_review(place_id):
    if request.method == 'POST':
        data = request.get_json()
        if 'user_id' in data and 'rating' in data and 'comment' in data:
            user_id = data['user_id']
            rating = data['rating']
            comment = data['comment']
            review = Review(place_id, user_id, rating, comment)
            reviews.append(review)
            return jsonify({'message': 'Review created successfully', 'review_id': review.review_id}), 201
        else:
            return jsonify({'error': 'Invalid input'}), 400

# Endpoint to retrieve all reviews for a place
@app.route('/places/<int:place_id>/reviews', methods=['GET'])
def get_reviews(place_id):
    if request.method == 'GET':
        place_reviews = [review.__dict__ for review in reviews if review.place_id == place_id]
        return jsonify(place_reviews), 200

# Endpoint to retrieve a specific review
@app.route('/places/<int:place_id>/reviews/<uuid:review_id>', methods=['GET'])  # Use UUID for review_id
def get_review(place_id, review_id):
    if request.method == 'GET':
        for review in reviews:
            if review.place_id == place_id and review.review_id == review_id:
                return jsonify(review.__dict__), 200
        return jsonify({'error': 'Review not found'}), 404

# Endpoint to update a review
@app.route('/places/<int:place_id>/reviews/<uuid:review_id>', methods=['PUT'])
def update_review(place_id, review_id):
    if request.method == 'PUT':
        data = request.get_json()
        for review in reviews:
            if review.place_id == place_id and review.review_id == review_id:
                review.rating = data.get('rating', review.rating)
                review.comment = data.get('comment', review.comment)
                review.updated_at = datetime.now()  # Update timestamp
                return jsonify({'message': 'Review updated successfully'}), 200
        return jsonify({'error': 'Review not found'}), 404

# Endpoint to delete a review
@app.route('/places/<int:place_id>/reviews/<uuid:review_id>', methods=['DELETE'])
def delete_review(place_id, review_id):
    if request.method == 'DELETE':
        for i, review in enumerate(reviews):
            if review.place_id == place_id and review.review_id == review_id:
                del reviews[i]
                return jsonify({'message': 'Review deleted successfully'}), 200
        return jsonify({'error': 'Review not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
