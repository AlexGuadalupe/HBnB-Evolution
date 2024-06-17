from persistence.IPersistenceManager import IPersistenceManager
import json
import datetime


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.isoformat()

        return super().default(o)


class DataManager(IPersistenceManager):
    """Clase para gestionar la persistencia de datos."""

    def __init__(self):
        """Inicializa el almacenamiento de datos."""
        self.storage = {}

    def create_user(self, user):
        """Crea un nuevo usuario."""
        user_id = len(self.storage) + 1
        user['id'] = user_id
        self.save(user)
        return user

    def save(self, entity):
        """Guarda una entidad en el almacenamiento."""
        entity_type = type(entity).__name__
        entity_id = getattr(entity, 'id', None)

        # guardar la entidad en un JSON file
        with open('data.json', 'w') as json_file:
            json.dump(entity, json_file, cls=DateTimeEncoder)

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

    def get_all_users(self):
        """Obtiene una lista de todos los usuarios."""
        return list(self.storage.values())

    def get_user_by_id(self, user_id):
        """Obtiene un usuario por su ID."""
        user = self.get(user_id, 'User')
        if user is None:
            return user

    def get_user_by_email(self, email):
        """Obtiene un usuario por su correo electrónico."""
        for entity_type, entities in self.storage.items():
            if entity_type == 'User':
                for entity in entities.values():
                    if entity.email == email:
                        return entity
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
