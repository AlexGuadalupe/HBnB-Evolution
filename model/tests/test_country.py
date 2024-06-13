import unittest
from datetime import datetime
# Suponiendo que el código de la clase Country está en un archivo llamado country.py
from model.country import Country


class TestCountry(unittest.TestCase):
    def setUp(self):
        self.id = 1
        self.name = "United States"
        self.code = "US"

    def test_initialization(self):
        country = Country(self.id, self.name, self.code)

        self.assertEqual(country.id, self.id)
        self.assertEqual(country.name, self.name)
        self.assertEqual(country.code, self.code)
        self.assertIsInstance(country.created_at, datetime)
        self.assertIsInstance(country.updated_at, datetime)
        self.assertLessEqual(country.created_at, datetime.now())
        self.assertLessEqual(country.updated_at, datetime.now())

    def test_country_count_increment(self):
        initial_count = Country.country_count
        Country(self.id, "Canada", "CA")
        self.assertEqual(Country.country_count, initial_count + 1)


if __name__ == '__main__':
    unittest.main()
