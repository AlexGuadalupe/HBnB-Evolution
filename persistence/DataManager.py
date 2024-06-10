from persistence.IPersistenceManager import IPersistenceManager
import json


class DataManager(IPersistenceManager):
    """Clase para gestionar la persistencia de datos."""

    def __init__(self):
        """Inicializa el almacenamiento de datos."""
        self.storage = {}

    def save(self, entity):
        """Guarda una entidad en el almacenamiento."""
        entity_type = type(entity).__name__
        entity_id = getattr(entity, 'id', None)
        if not entity_id:
            raise ValueError("Entity must have an 'id' attribute.")

        if entity_type not in self.storage:
            self.storage[entity_type] = {}

        self.storage[entity_type][entity_id] = entity
        print(f"Saved entity: {entity}")

    def get(self, entity_id, entity_type):
        """Recupera una entidad por ID y tipo del almacenamiento."""
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            return self.storage[entity_type][entity_id]
        else:
            print(f"Entity not found: {entity_type} with ID {entity_id}")
            return None

    def update(self, entity):
        """Actualiza una entidad existente en el almacenamiento."""
        entity_type = type(entity).__name__
        entity_id = getattr(entity, 'id', None)
        if not entity_id:
            raise ValueError("Entity must have an 'id' attribute.")

        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            self.storage[entity_type][entity_id] = entity
            print(f"Updated entity: {entity}")
        else:
            print(f"Entity not found: {entity_type} with ID {entity_id}")

    def delete(self, entity_id, entity_type):
        """Elimina una entidad por ID y tipo del almacenamiento."""
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]
            print(f"Deleted entity: {entity_type} with ID {entity_id}")
        else:
            print(f"Entity not found: {entity_type} with ID {entity_id}")
