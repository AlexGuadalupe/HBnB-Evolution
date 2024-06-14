import uuid
from model.BaseModel import BaseModel


class User(BaseModel):
    user_count = 0
    email_set = set()

    def __init__(self, email, first_name, last_name):

        if not self.validate_email(email):
            raise ValueError("Invalid email address")
        if email in User.email_set:
            raise ValueError("Email already in use")

        self.id = uuid.uuid4()
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

        User.email_set.add(email)
        User.user_count += 1
        super().__init__()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email
