class Amenity:
    amenity_count = 0

    def __init__(self, name, description):
        self.amenity_id = Amenity.amenity_count + 1
        self.name = name
        self.description = description
        Amenity.amenity_count += 1

    def __repr__(self):
        return f"Amenity({self.amenity_id}, {self.name}, {self.description})"
