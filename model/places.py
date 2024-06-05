import uuid
from datetime import datetime

class Places:
    places_count = 0

    def __init__(self, name, description, location, user_id):
        self.places_id = uuid.uuid4()
        self.name = name
        self.description = description
        self.location = location
        self.user_id = user_id
        self.amenities = []
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        Places.places_count += 1

    def add_amenities(self, amenities):
        if amenities not in self.amenities:
            self.amenities.append(amenities)
            self.updated_at = datetime.now()