import unittest
import uuid
from datetime import datetime
# Suponiendo que el código de la clase Place está en un archivo llamado place.py
from model.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.name = "Cozy Cottage"
        self.location = "Countryside"
        self.owner = "John Doe"
        self.description = "A cozy cottage in the woods"
        self.address = "123 Forest Lane"
        self.city = "Forest City"
        self.latitude = 34.052235
        self.longitude = -118.243683
        self.price_per_night = 100
        self.amenity = "WiFi"
        self.review_content = "Beautiful location, loved staying here!"

    def test_initialization(self):
        place = Place(self.name, self.location, self.owner, description=self.description,
                      address=self.address, city=self.city, latitude=self.latitude,
                      longitude=self.longitude, price_per_night=self.price_per_night)

        self.assertIsInstance(place.place_id, uuid.UUID)
        self.assertEqual(place.name, self.name)
        self.assertEqual(place.location, self.location)
        self.assertEqual(place.owner, self.owner)
        self.assertEqual(place.description, self.description)
        self.assertEqual(place.address, self.address)
        self.assertEqual(place.city, self.city)
        self.assertEqual(place.latitude, self.latitude)
        self.assertEqual(place.longitude, self.longitude)
        self.assertEqual(place.price_per_night, self.price_per_night)
        self.assertEqual(place.reviews, [])
        self.assertEqual(place.amenities, [])

    def test_add_review(self):
        place = Place(self.name, self.location, self.owner)
        place.add_review(self.review_content)
        self.assertEqual(len(place.reviews), 1)
        self.assertEqual(place.reviews[0], self.review_content)

    def test_add_amenities(self):
        place = Place(self.name, self.location, self.owner)
        place.add_amenities(self.amenity)
        self.assertIn(self.amenity, place.amenities)

    def test_duplicate_place_host(self):
        Place.clear_places_hosts()  # Limpiar el diccionario _places_hosts
        Place(self.name, self.location, self.owner)
        with self.assertRaises(ValueError):
            Place(self.name, "Downtown", "Jane Doe")

    @classmethod
    def tearDownClass(cls):
        # Limpiar el diccionario _places_hosts al finalizar las pruebas
        Place.clear_places_hosts()


if __name__ == '__main__':
    unittest.main()
