import unittest
from model.amenities import Amenities


class TestAmenities(unittest.TestCase):

    def setUp(self):
        Amenities.amenities_count = 0

    def test_amenities_creation(self):
        amenities = Amenities("Free WiFi", "High-speed internet access")
        self.assertEqual(amenities.amenities_id, 1)
        self.assertEqual(amenities.name, "Free WiFi")
        self.assertEqual(amenities.description, "High-speed internet access")
        self.assertIsNotNone(amenities.created_at)
        self.assertIsNotNone(amenities.updated_at)


if __name__ == '__main__':
    unittest.main()
