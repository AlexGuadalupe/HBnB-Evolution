import unittest
import uuid
from model.BaseModel import BaseModel
# Suponiendo que el código de la clase Review está en un archivo llamado review.py
from model.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        self.content = "Great place!"
        self.rating = 5
        self.user_id = str(uuid.uuid4())
        self.place_id = str(uuid.uuid4())

    def test_initialization(self):
        review = Review(self.content, self.rating, self.user_id, self.place_id)
        self.assertEqual(review.content, self.content)
        self.assertEqual(review.rating, self.rating)
        self.assertEqual(review.user_id, self.user_id)
        self.assertEqual(review.place_id, self.place_id)

    def test_rating_validation(self):
        with self.assertRaises(ValueError):
            Review(self.content, 0, self.user_id, self.place_id)

        with self.assertRaises(ValueError):
            Review(self.content, 6, self.user_id, self.place_id)

    def test_review_count_increment(self):
        initial_count = Review.review_count
        Review(self.content, self.rating, self.user_id, self.place_id)
        self.assertEqual(Review.review_count, initial_count + 1)


if __name__ == '__main__':
    unittest.main()
