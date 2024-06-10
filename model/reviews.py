import uuid
from model import BaseModel


class Review(BaseModel):
    review_count = 0

    def __init__(self, content, rating, user_id, place_id):
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")

        self.content = content
        self.rating = rating
        self.user_id = user_id
        self.place_id = place_id

        Review.review_count += 1
