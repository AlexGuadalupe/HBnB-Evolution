import uuid
from datetime import datetime

class Amenities:
    amenities_count = 0

    def __init__(self, name, description):
        self.amenities_id = uuid.uuid4()
        self.name = name
        self.description = description
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        Amenities.amenities_count += 1