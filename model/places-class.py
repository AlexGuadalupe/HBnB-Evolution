class Place:
    place_count = 0

    def __init__(self, name, description, location, user_id):
        self.place_id = Place.place_count + 1
        self.name = name
        self.description = description
        self.location = location
        self.user_id = user_id
        Place.place_count += 1

    def __repr__(self):
        return f"Place({self.place_id}, {self.name}, {self.description}, {self.location}, {self.user_id})"
