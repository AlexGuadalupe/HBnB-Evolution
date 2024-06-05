import uuid
from datetime import datetime

class City:
    city_count = 0

    def __init__(self, name, country_id):
        self.city_id = uuid.uuid4()
        self.name = name
        self.country_id = country_id
        self.created_at = datetime.now()
        self.updated_at = self.created_at

        City.city_count += 1