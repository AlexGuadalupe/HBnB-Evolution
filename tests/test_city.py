import unittest
from model.city import City
from model.country import Country


class TestCity(unittest.TestCase):

    def setUp(self):
        City.city_count = 0
        Country.country_count = 0
        self.country = Country("USA")

    def test_city_creation(self):
        city = City("New York", self.country.country_id)
        self.assertEqual(city.city_id, 1)
        self.assertEqual(city.name, "New York")
        self.assertEqual(city.country_id, self.country.country_id)
        self.assertIsNotNone(city.created_at)
        self.assertIsNotNone(city.updated_at)

    def test_city_invalid_country(self):
        with self.assertRaises(ValueError):
            City("New York", 999)


if __name__ == '__main__':
    unittest.main()
