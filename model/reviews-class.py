import uuid
from datetime import datetime

class Review:
    review_count = 0

    def __init__(self, content, rating, user_id, place_id):
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")

        self.review_id = uuid.uuid4()
        self.content = content
        self.rating = rating
        self.user_id = user_id
        self.place_id = place_id
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        Review.review_count += 1