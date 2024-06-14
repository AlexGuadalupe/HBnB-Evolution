import unittest
import uuid
from model.city import City  # Importa la clase City desde el módulo city


class TestCity(unittest.TestCase):
    def setUp(self):
        self.name = "New York"
        self.country = "USA"
        self.city = City(self.name, self.country)

    def test_initialization(self):
        self.assertEqual(self.city.name, self.name)
        self.assertEqual(self.city.country, self.country)
        # Verifica que places se inicializa como una lista vacía
        self.assertIsInstance(self.city.places, list)

    def test_add_place(self):
        place_id = uuid.uuid4()
        self.city.add_place(place_id)
        self.assertIn(place_id, self.city.places)
        # Verifica que se haya añadido un solo lugar
        self.assertEqual(len(self.city.places), 1)

    def test_add_duplicate_place(self):
        place_id = uuid.uuid4()
        self.city.add_place(place_id)
        # Intentar añadir el mismo lugar nuevamente
        self.city.add_place(place_id)
        # Verifica que el tamaño de places no haya cambiado


if __name__ == '__main__':
    unittest.main()
