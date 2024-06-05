import unittest
from model.review import Review
from model.user import User
from model.place import Place


class TestReview(unittest.TestCase):

    def setUp(self):
        Review.review_count = 0
        User.user_count = 0
        User.email_set = set()
        Place.place_count = 0
        self.user = User("reviewer@example.com", "Review", "User")
        self.place = Place(
            "Central Park", "A large public park in NYC", "New York, NY", self.user.user_id)

    def test_review_creation(self):
        review = Review("Great place!", 5, self.user.user_id,
                        self.place.place_id)
        self.assertEqual(review.review_id, 1)
        self.assertEqual(review.content, "Great place!")
        self.assertEqual(review.rating, 5)
        self.assertIsNotNone(review.created_at)
        self.assertIsNotNone(review.updated_at)

    def test_review_invalid_rating(self):
        with self.assertRaises(ValueError):
            Review("Bad place!", 10, self.user.user_id, self.place.place_id)

    def test_review_user_place_association(self):
        review = Review("Great place!", 5, self.user.user_id,
                        self.place.place_id)
        self.assertEqual(review.user_id, self.user.user_id)
        self.assertEqual(review.place_id, self.place.place_id)


if __name__ == '__main__':
    unittest.main()
