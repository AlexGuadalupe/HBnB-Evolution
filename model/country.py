from model import BaseModel


class Country(BaseModel):
    country_count = 0

    def __init__(self, name, country_id):
        self.name = name
        self.country_id = country_id
        Country.country_count += 1

    def __repr__(self):
        return f"Country({self.name}, {self.country_id})"
