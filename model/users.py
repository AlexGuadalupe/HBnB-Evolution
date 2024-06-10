import uuid
from model import BaseModel


class User:
    user_count = 0
    email_set = set()

    def __init__(self, email, first_name, last_name):
        if not self.validate_email(email):
            raise ValueError("Invalid email address")
        if email in User.email_set:
            raise ValueError("Email already in use")

        self.email = email
        self.first_name = first_name
        self.last_name = last_name

        User.email_set.add(email)
        User.user_count += 1

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    @staticmethod
    def validate_email(email):
        # Simple email validation for example purposes
        return "@" in email and "." in email
