from flask import Flask, request, jsonify
app = Flask(__name__)

# In-memory dictionary to store review data
reviews = {}

# Review data model
class Review:
    def __init__(self, place_id, user_id, rating, comment):
        self.place_id = place_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment

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
            reviews[place_id] = reviews.get(place_id, [])
            reviews[place_id].append(review.__dict__)
            return jsonify({'message': 'Review created successfully'}), 201
        else:
            return jsonify({'error': 'Invalid input'}), 400

# Endpoint to retrieve all reviews for a place
@app.route('/places/<int:place_id>/reviews', methods=['GET'])
def get_reviews(place_id):
    if request.method == 'GET':
        return jsonify(reviews.get(place_id, [])), 200

# Endpoint to retrieve a specific review for a place
@app.route('/places/<int:place_id>/reviews/<int:review_id>', methods=['GET'])
def get_review(place_id, review_id):
    if request.method == 'GET':
        place_reviews = reviews.get(place_id, [])
        for review in place_reviews:
            if review['place_id'] == place_id and review['user_id'] == review_id:
                return jsonify(review), 200
        return jsonify({'error': 'Review not found'}), 404

# Endpoint to update a review
@app.route('/places/<int:place_id>/reviews/<int:review_id>', methods=['PUT'])
def update_review(place_id, review_id):
    if request.method == 'PUT':
        data = request.get_json()
        place_reviews = reviews.get(place_id, [])
        for review in place_reviews:
            if review['place_id'] == place_id and review['user_id'] == review_id:
                review['rating'] = data.get('rating', review['rating'])
                review['comment'] = data.get('comment', review['comment'])
                return jsonify({'message': 'Review updated successfully'}), 200
        return jsonify({'error': 'Review not found'}), 404

# Endpoint to delete a review
@app.route('/places/<int:place_id>/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(place_id, review_id):
    if request.method == 'DELETE':
        place_reviews = reviews.get(place_id, [])
        for review in place_reviews:
            if review['place_id'] == place_id and review['user_id'] == review_id:
                place_reviews.remove(review)
                return jsonify({'message': 'Review deleted successfully'}), 200
        return jsonify({'error': 'Review not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
