import unittest
from model.place import Place
from model.user import User


class TestPlace(unittest.TestCase):

    def setUp(self):
        Place.place_count = 0
        User.user_count = 0
        User.email_set = set()
        self.user = User("host@example.com", "Host", "User")

    def test_place_creation(self):
        place = Place("Central Park", "A large public park in NYC",
                      "New York, NY", self.user.user_id)
        self.assertEqual(place.place_id, 1)
        self.assertEqual(place.name, "Central Park")
        self.assertIsNotNone(place.created_at)
        self.assertIsNotNone(place.updated_at)

    def test_add_amenity(self):
        place = Place("Central Park", "A large public park in NYC",
                      "New York, NY", self.user.user_id)
        place.add_amenity("Free WiFi")
        self.assertIn("Free WiFi", place.amenities)
        self.assertNotEqual(place.created_at, place.updated_at)

    def test_place_host_assignment(self):
        place = Place("Central Park", "A large public park in NYC",
                      "New York, NY", self.user.user_id)
        self.assertEqual(place.user_id, self.user.user_id)

    def test_place_invalid_host(self):
        with self.assertRaises(ValueError):
            Place("Central Park", "A large public park in NYC", "New York, NY", 999)


if __name__ == '__main__':
    unittest.main()
