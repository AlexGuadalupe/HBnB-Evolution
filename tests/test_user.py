import unittest
from model.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        User.user_count = 0
        User.email_set = set()

    def test_user_creation(self):
        user = User("test@example.com", "John", "Doe")
        self.assertEqual(user.user_id, 1)
        self.assertEqual(user.email, "test@example.com")

    def test_duplicate_email(self):
        User("test@example.com", "John", "Doe")
        with self.assertRaises(ValueError):
            User("test@example.com", "Jane", "Doe")


if __name__ == '__main__':
    unittest.main()
