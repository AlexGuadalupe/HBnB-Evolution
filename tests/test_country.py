import unittest
from model.country import Country
from datetime import datetime


class TestCountry(unittest.TestCase):

    def setUp(self):
        Country.country_count = 0

    def test_country_creation(self):
        country = Country("Puerto Rico", "PR")
        self.assertEqual(country.country_id, "PR" )
        self.assertEqual(country.name, "Puerto Rico")
        self.assertIsNotNone(country.created_at)
        self.assertIsNotNone(country.updated_at)
        self.assertTrue(isinstance(country.created_at, datetime))
        self.assertTrue(isinstance(country.updated_at, datetime))






if __name__ == '__main__':
    unittest.main()
