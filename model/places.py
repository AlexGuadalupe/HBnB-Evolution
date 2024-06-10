import uuid
from datetime import datetime

class Places:
    places_count = 0

    def __init__(self, name, description, address, city_id, latitude,
                 longitude, host_id, number_of_rooms, number_of_bathrooms,
                 price_per_night,max_guests, amenities_ids):
        self.places_id = uuid.uuid4()
        self.name = name
        self.description = description
        self.address = address
        self.city_id = city_id
        self.latitude = latitude
        self.longitude = longitude
        self.host_id = host_id
        self.number_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenities_ids = []
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        Places.places_count += 1

    def add_amenities(self, amenities):
        if amenities not in self.amenities:
            self.amenities.append(amenities)
            self.updated_at = datetime.now()