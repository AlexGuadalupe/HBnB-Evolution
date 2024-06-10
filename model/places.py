import uuid
from model import BaseModel


class Places(BaseModel):
    places_count = 0

    def __init__(self, name, description, location, user_id):
        self.name = name
        self.description = description
        self.location = location
        self.user_id = user_id
        self.amenities = []

        Places.places_count += 1

    def add_amenities(self, amenities):
        if amenities not in self.amenities:
            self.amenities.append(amenities)
