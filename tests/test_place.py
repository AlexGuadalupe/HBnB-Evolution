import unittest
from model.place import Place


class TestPlace(unittest.TestCase):

    def setUp(self):
        Place.place_count = 0

    def test_place_creation(self):
        place = Place("Central Park",
                      "A large public park in NYC", "New York, NY", 1)
        self.assertEqual(place.place_id, 1)
        self.assertEqual(place.name, "Central Park")


if __name__ == '__main__':
    unittest.main()
