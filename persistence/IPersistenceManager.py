from abc import ABC, abstractmethod


class IPersistenceManager(ABC):
    """Interfaz que define métodos para operaciones CRUD en gestión de datos."""

    @abstractmethod
    def save(self, entity):
        """Guarda una entidad en el almacenamiento."""
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        """Recupera una entidad por ID y tipo del almacenamiento."""
        pass

    @abstractmethod
    def update(self, entity):
        """Actualiza una entidad existente en el almacenamiento."""
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        """Elimina una entidad por ID y tipo del almacenamiento."""
        pass
