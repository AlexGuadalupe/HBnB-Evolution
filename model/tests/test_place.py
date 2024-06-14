import unittest
from model.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.name = "Cozy Cabin"
        self.location = "Mountain"
        self.owner = "John Doe"
        self.description = "A cozy cabin in the mountains"
        self.address = "123 Mountain Road"
        self.city = "Mountain Town"
        self.latitude = 42.1234
        self.longitude = -78.5678
        self.price_per_night = 100
        self.place = Place(self.name, self.location, self.owner, description=self.description,
                           address=self.address, city=self.city, latitude=self.latitude,
                           longitude=self.longitude, price_per_night=self.price_per_night)

    def tearDown(self):
        Place.clear_places_hosts()

    def test_initialization(self):
        self.assertEqual(self.place.name, self.name)
        self.assertEqual(self.place.location, self.location)
        self.assertEqual(self.place.owner, self.owner)
        self.assertEqual(self.place.description, self.description)
        self.assertEqual(self.place.address, self.address)
        self.assertEqual(self.place.city, self.city)
        self.assertEqual(self.place.latitude, self.latitude)
        self.assertEqual(self.place.longitude, self.longitude)
        self.assertEqual(self.place.price_per_night, self.price_per_night)
        self.assertEqual(self.place.reviews, [])
        self.assertEqual(self.place.amenities, [])

    def test_add_review(self):
        review = "Great place to stay!"
        self.place.add_review(review)
        self.assertEqual(len(self.place.reviews), 1)
        self.assertEqual(self.place.reviews[0], review)

    def test_add_amenities(self):
        amenity = "WiFi"
        self.place.add_amenities(amenity)
        self.assertEqual(len(self.place.amenities), 1)
        self.assertEqual(self.place.amenities[0], amenity)

    def test_clear_places_hosts(self):
        # Add a place to _places_hosts
        Place.clear_places_hosts()
        self.assertEqual(len(Place._places_hosts), 0)

    def test_duplicate_place_host(self):
        # Adding the same place name and owner should raise ValueError
        with self.assertRaises(ValueError):
            Place(self.name, self.location, self.owner)


if __name__ == '__main__':
    unittest.main()
