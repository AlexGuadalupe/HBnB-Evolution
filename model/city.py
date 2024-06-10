import uuid
from model import BaseModel


class City(BaseModel):
    city_count = 0

    def __init__(self, name, country_id):
        self.name = name
        self.country_id = country_id

        City.city_count += 1
