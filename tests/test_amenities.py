import unittest
from model.amenities import Amenities
import uuid


class TestAmenities(unittest.TestCase):

    def setUp(self):
        Amenities.amenities_count = 0

    def test_amenities_creation(self):
        amenities = Amenities("Free WiFi", "High-speed internet access")
        self.assertIsInstance(amenities.amenities_id, uuid.UUID)
        self.assertEqual(amenities.name, "Free WiFi")
        self.assertEqual(amenities.description, "High-speed internet access")
        self.assertIsNotNone(amenities.created_at)
        self.assertIsNotNone(amenities.updated_at)
        self.assertEqual(amenities.created_at, amenities.updated_at)


if __name__ == '__main__':
    unittest.main()
