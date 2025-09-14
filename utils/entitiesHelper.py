# Entity helper function       
from utils.constants import EXCLUDED_PRINT_HEADERS


def get_next_id(matriz):
    return len(matriz) + 1

def create_arrays():
    owners = [
        [1, "35125487", "Ana", "Pérez", "ana.perez@example.com", "1144441111", True],
        [2, "45785126", "Bruno", "Silva", "bruno.silva@example.com", "1144442222", True],
        [3, "52654789", "Carla", "Gómez", "carla.gomez@example.com", "1144443333", True],
        [4, "28745963", "David", "López", "david.lopez@example.com", "1144444444", True],
        [5, "39158742", "Elena", "Ramírez", "elena.ramirez@example.com", "1144445555", True],
        [6, "41589632", "Franco", "Torres", "franco.torres@example.com", "1144446666", False],
    ]
    mascotas = [
        [1, "Milo", "Perro", "Labrador", 5, 1, 23.5, "Macho", True],
        [2, "Luna", "Gato", "Siamés", 3, 1, 4.2, "Hembra", True],
        [3, "Rocky", "Perro", "Bulldog", 4, 2, 20.0, "Macho", True],
        [4, "Nina", "Gato", "Común europeo", 2, 3, 3.8, "Hembra", True],
        [5, "Simba", "Gato", "Persa", 6, 4, 5.5, "Macho", True],
        [6, "Toby", "Perro", "Beagle", 7, 5, 12.0, "Macho", True],
        [7, "Molly", "Perro", "Golden Retriever", 1, 6, 25.0, "Hembra", True],
        [8, "Kira", "Gato", "Maine Coon", 4, 5, 6.0, "Hembra", True],
        [9, "Firulais", "Perro", "Mestizo", 8, 4, 15.0, "Macho", False],
    ]
    turnos = [
        [1, 1, "15-08-2025", "10:00", "Extraccion", 1, True],
        [2, 2, "16-08-2025", "11:30", "Operacion", 3, True],
        [3, 4, "16-08-2025", "10:00", "Chequeo anual", 1, True],
        [4, 3, "17-08-2025", "09:00", "Triple gatuna", 3, True],
        [5, 5, "18-08-2025", "14:00", "Operacion", 1, True],
        [6, 6, "18-08-2025", "15:30", "Vacunación", 2, False],
        [7, 7, "19-08-2025", "11:00", "Chequeo anual", 3, True],
        [8, 8, "19-08-2025", "12:00", "Vacunación", 1, True],
    ]
    veterinarians = [
        [1, "36485787", "Martín", "Herrera", "MN12345", "mherrera@gmail.com", "1155551111", True],
        [2, "17456321", "Camila", "Álvarez", "MN54321", "calvare@gmail.com", "1155552222", False],
        [3, "34125478", "Julián", "Duarte", "MN98765", "jdurate@gmail.com", "1155553333", True],
        [4, "40157896", "Sofía", "Castro", "MN78965", "scastro@gmail.com", "1155554444", True],
        [5, "25874123", "Pedro", "García", "MN45678", "pgarcia@gmail.com", "1155555555", True],
        [6, "42154789", "Laura", "Díaz", "MN15975", "ldiaz@gmail.com", "1155556666", False],
    ]

    return owners, mascotas, turnos, veterinarians

def update_entity_data(entity, headers):
    """Updates an entity's data based on user input for each field.

    Iterates over the provided headers and prompts the user to input a new
    value for each field, except those listed in EXCLUDED_PRINT_HEADERS.
    Returns a new entity list with the updated values.

    Args:
        entity (list): The current entity record represented as a list of values.
        headers (list[str]): The headers corresponding to the entity's fields.

    Returns:
        list: A new list representing the updated entity.
    """
    updated_entity = entity.copy()
    for header in headers:
        if header in EXCLUDED_PRINT_HEADERS:
            continue
        index = headers.index(header)
        input_header = input(f'Ingresa {header}: ')
        updated_entity[index] = input_header 
    return updated_entity