import unittest
from model.review import Review


class TestReview(unittest.TestCase):

    def setUp(self):
        Review.review_count = 0

    def test_review_creation(self):
        review = Review("Great place!", 5, 1, 1)
        self.assertEqual(review.review_id, 1)
        self.assertEqual(review.content, "Great place!")


if __name__ == '__main__':
    unittest.main()
