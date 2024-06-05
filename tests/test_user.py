import unittest
from model.user import User
from datetime import datetime
import uuid


class TestUser(unittest.TestCase):

    def setUp(self):
        User.user_count = 0
        User.email_set = set()

    def test_user_creation(self):
        user = User("test@example.com", "John", "Doe")
        self.assertIsInstance(user.user_id, uuid.UUID)
        self.assertEqual(user.email, "test@example.com")
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)
        self.assertEqual(user.created_at, user.updated_at)

    def test_duplicate_email(self):
        User("test@example.com", "John", "Doe")
        with self.assertRaises(ValueError):
            User("test@example.com", "Jane", "Doe")

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            User("invalid-email", "John", "Doe")

    def test_user_update(self):
        user = User("test@example.com", "John", "Doe")
        original_updated_at = user.updated_at
        user.update(first_name="Johnny", last_name="Smith")
        self.assertEqual(user.first_name, "Johnny")
        self.assertEqual(user.last_name, "Smith")
        self.assertGreater(user.updated_at, original_updated_at)


if __name__ == '__main__':
    unittest.main()
