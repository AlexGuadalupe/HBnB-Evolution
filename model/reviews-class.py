class Review:
    review_count = 0

    def __init__(self, content, rating, user_id, place_id):
        self.review_id = Review.review_count + 1
        self.content = content
        self.rating = rating
        self.user_id = user_id
        self.place_id = place_id
        Review.review_count += 1

    def __repr__(self):
        return f"Review({self.review_id}, {self.content}, {self.rating}, {self.user_id}, {self.place_id})"
