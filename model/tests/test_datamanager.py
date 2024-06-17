import unittest
from persistence import DataManager
from dataclasses import dataclass


@dataclass
class Entity:
    id: str
    name: str


class TestDataManager(unittest.TestCase):

    def setUp(self):
        """Configura el entorno de prueba antes de cada prueba."""
        self.DataManager = DataManager()
        self.entity = Entity(id="1", name="Test Entity")

    def test_get_user_by_id(self):
        user_id = '123'  # Reemplaza esto con un ID de usuario válido
        user = self.data_manager.get_user_by_id(user_id)
        self.assertIsNotNone(user, "No se encontró el usuario.")
        self.assertEqual(user.id, user_id, "El ID del usuario no coincide.")

    def test_save_entity(self):
        """Prueba el método save."""
        self.DataManager.save(self.entity)
        retrieved_entity = self.DataManager.get(self.entity.id, 'Entity')
        self.assertIsNotNone(retrieved_entity)
        self.assertEqual(retrieved_entity.id, self.entity.id)
        self.assertEqual(retrieved_entity.name, self.entity.name)

    def test_get_entity_not_found(self):
        """Prueba el método get cuando la entidad no existe."""
        retrieved_entity = self.DataManager.get("2", 'Entity')
        self.assertIsNone(retrieved_entity)

    def test_update_entity(self):
        """Prueba el método update."""
        self.DataManager.save(self.entity)
        self.entity.name = "Updated Entity"
        self.DataManager.update(self.entity)
        retrieved_entity = self.DataManager.get(self.entity.id, 'Entity')
        self.assertIsNotNone(retrieved_entity)
        self.assertEqual(retrieved_entity.name, "Updated Entity")

    def test_update_entity_not_found(self):
        """Prueba la actualización de una entidad que no existe."""
        new_entity = Entity(id="2", name="New Entity")
        self.DataManager.update(new_entity)
        retrieved_entity = self.DataManager.get(new_entity.id, 'Entity')
        self.assertIsNone(retrieved_entity)

    def test_delete_entity(self):
        """Prueba el método delete."""
        self.DataManager.save(self.entity)
        self.DataManager.delete(self.entity.id, 'Entity')
        retrieved_entity = self.DataManager.get(self.entity.id, 'Entity')
        self.assertIsNone(retrieved_entity)

    def test_delete_entity_not_found(self):
        """Prueba la eliminación de una entidad que no existe."""
        self.DataManager.delete("2", 'Entity')
        # No hay nada específico que verificar aquí, solo aseguramos que no cause un error.

    def test_save_entity_without_id(self):
        """Prueba que se lance una excepción si la entidad no tiene un atributo 'id'."""
        invalid_entity = Entity(id=None, name="Invalid Entity")
        with self.assertRaises(ValueError):
            self.DataManager.save(invalid_entity)


if __name__ == '__main__':
    unittest.main()
