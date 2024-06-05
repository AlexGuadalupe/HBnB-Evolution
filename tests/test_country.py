import unittest
from model.country import Country


class TestCountry(unittest.TestCase):

    def setUp(self):
        Country.country_count = 0

    def test_country_creation(self):
        country = Country("USA")
        self.assertEqual(country.country_id, 1)
        self.assertEqual(country.name, "USA")
        self.assertIsNotNone(country.created_at)
        self.assertIsNotNone(country.updated_at)


if __name__ == '__main__':
    unittest.main()
