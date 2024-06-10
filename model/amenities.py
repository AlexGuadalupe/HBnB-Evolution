import uuid
from model import BaseModel


class Amenities(BaseModel):
    amenities_count = 0

    def __init__(self, name, description):
        self.name = name
        self.description = description

        Amenities.amenities_count += 1
