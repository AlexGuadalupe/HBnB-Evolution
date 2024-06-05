from datetime import datetime

class Country:
    country_count = 0

    def __init__(self, name, country_id):
        self.name = name
        self.country_id = country_id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        Country.country_count += 1
    def __repr__(self):
        return f"Country({self.name}, {self.country_id})"
