class User:
    user_count = 0
    email_set = set()

    def __init__(self, email, first_name, last_name):
        if email in User.email_set:
            raise ValueError("Email already exists")
        self.user_id = User.user_count + 1
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        User.user_count += 1
        User.email_set.add(email)

    def __repr__(self):
        return f"User({self.user_id}, {self.email}, {self.first_name}, {self.last_name})"
