import unittest

from model.users import User
from app import app


class TestUser(unittest.TestCase):

    def setUp(self):
        User.user_count = 0
        User.email_set = set()

    def test_user_creation(self):
        user = User(email="test@example.com",
                    first_name="John", last_name="Doe")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(User.user_count, 1)
        self.assertIn("test@example.com", User.email_set)

    def test_duplicate_email(self):
        User(email="test@example.com", first_name="John", last_name="Doe")
        with self.assertRaises(ValueError) as context:
            User(email="test@example.com", first_name="Jane", last_name="Smith")
        self.assertEqual(str(context.exception), "Email already in use")

    def test_invalid_email(self):
        with self.assertRaises(ValueError) as context:
            User(email="invalid-email", first_name="John", last_name="Doe")
        self.assertEqual(str(context.exception), "Invalid email address")

    def test_user_update(self):
        user = User(email="test@example.com",
                    first_name="John", last_name="Doe")
        user.update(first_name="Jane", last_name="Smith")
        self.assertEqual(user.first_name, "Jane")
        self.assertEqual(user.last_name, "Smith")

    def test_user_unique_id(self):
        user1 = User(email="test1@example.com",
                     first_name="John", last_name="Doe")
        user2 = User(email="test2@example.com",
                     first_name="Jane", last_name="Smith")
        self.assertNotEqual(user1.id, user2.id)


if __name__ == "__main__":
    unittest.main()
