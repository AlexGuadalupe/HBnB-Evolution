import uuid
from datetime import datetime

class User:
    user_count = 0
    email_set = set()

    def __init__(self, email, first_name, last_name):
        if not self.validate_email(email):
            raise ValueError("Invalid email address")
        if email in User.email_set:
            raise ValueError("Email already in use")

        self.user_id = uuid.uuid4()
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        User.email_set.add(email)
        User.user_count += 1

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.updated_at = datetime.now()

    @staticmethod
    def validate_email(email):
        # Simple email validation for example purposes
        return "@" in email and "." in email