class City:
    city_count = 0

    def __init__(self, name, country_id):
        self.city_id = City.city_count + 1
        self.name = name
        self.country_id = country_id
        City.city_count += 1

    def __repr__(self):
        return f"City({self.city_id}, {self.name}, {self.country_id})"
