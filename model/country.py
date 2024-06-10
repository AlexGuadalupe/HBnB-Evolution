from datetime import datetime

class Country:
    country_count = 0

    def __init__(self, id, name, code):
        self.name = name
        self.id = id
        self.code = code
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        Country.country_count += 1

    def __repr__(self):
        return f"Country({self.name}, {self.country_id})"
