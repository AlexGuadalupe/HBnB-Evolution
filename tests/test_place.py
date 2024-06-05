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
        place = Place("Santurce", "A rural San Juan area.",
                      "San Juan, PR", self.user.user_id)
        self.assertEqual(place.place_id, 1)
        self.assertEqual(place.name, "Santurce")
        self.assertIsNotNone(place.created_at)
        self.assertIsNotNone(place.updated_at)

    def test_add_amenities(self):
        place = Place("Santurce", "A rural San Juan area.",
                      "San Juan, PR", self.user.user_id)
        place.add_amenity("Jacuzzi")
        self.assertIn("Jacuzzi", place.amenities)
        self.assertNotEqual(place.created_at, place.updated_at)

    def test_place_host_assignment(self):
        place = Place("Santurce", "A rural San Juan area.",
                      "San Juan, PR", self.user.user_id)
        self.assertEqual(place.user_id, self.user.user_id)

    def test_place_invalid_host(self):
        with self.assertRaises(ValueError):
            Place("Santurce", "A rural San Juan area", "San Juan, PR", 00909)


if __name__ == '__main__':
    unittest.main()
