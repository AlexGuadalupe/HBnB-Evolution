import unittest
from model.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def setUp(self):
        Amenity.amenity_count = 0

    def test_amenity_creation(self):
        amenity = Amenity("Free WiFi", "High-speed internet access")
        self.assertEqual(amenity.amenity_id, 1)
        self.assertEqual(amenity.name, "Free WiFi")
        self.assertEqual(amenity.description, "High-speed internet access")
        self.assertIsNotNone(amenity.created_at)
        self.assertIsNotNone(amenity.updated_at)


if __name__ == '__main__':
    unittest.main()
