class Amenities:
    amenities_count = 0

    def __init__(self, name, description):
        self.amenities_id = Amenities.amenities_count + 1
        self.name = name
        self.description = description
        Amenities.amenities_count += 1

    def __repr__(self):
        return f"Amenities({self.amenities_id}, {self.name}, {self.description})"
