class Country:
    country_count = 0

    def __init__(self, name):
        self.country_id = Country.country_count + 1
        self.name = name
        Country.country_count += 1

    def __repr__(self):
        return f"Country({self.country_id}, {self.name})"
