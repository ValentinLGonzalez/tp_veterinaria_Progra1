# Entity helper function       
from utils.constants import EXCLUDED_PRINT_HEADERS


def get_next_id(matriz):
    return len(matriz) + 1

def create_arrays():
    owners = [
        [1, "35125487", "Ana", "Pérez", "ana.perez@example.com", "1144441111", True],
        [2, "45785126", "Bruno", "Silva", "bruno.silva@example.com", "1144442222", True],
        [3, "52654789", "Carla", "Gómez", "carla.gomez@example.com", "1144443333", True],
        [4, "30123456", "Diego", "Rodríguez", "diego.rod@example.com", "1144444444", True],
        [5, "28987654", "Elena", "Torres", "elena.torres@example.com", "1144445555", True],
        [6, "33445566", "Fernando", "López", "fer.lopez@example.com", "1144446666", False],
        [7, "41234567", "Gabriela", "Martínez", "gabi.mart@example.com", "1144447777", True],
        [8, "39876543", "Héctor", "García", "hector.garcia@example.com", "1144448888", True]
    ]

    mascotas = [
        [1, "Milo", "Perro", "Labrador", 5, 1, 23.5, "Macho", True],
        [2, "Luna", "Gato", "Siamés", 3, 1, 4.2, "Hembra", True],
        [3, "Rocky", "Perro", "Bulldog", 4, 2, 20.0, "Macho", True],
        [4, "Nina", "Gato", "Común europeo", 2, 3, 3.8, "Hembra", True],
        [5, "Max", "Perro", "Golden Retriever", 2, 4, 18.0, "Macho", True],
        [6, "Bella", "Perro", "Chihuahua", 1, 5, 2.5, "Hembra", True],
        [7, "Simba", "Gato", "Persa", 4, 7, 5.1, "Macho", True],
        [8, "Coco", "Perro", "Caniche", 3, 8, 6.8, "Macho", True],
        [9, "Lola", "Gato", "Angora", 2, 5, 3.9, "Hembra", False]
    ]

    turnos = [
        [1, 1, "15.08.2025", "10:00", "Extracción de sangre", 1, True],
        [2, 2, "16.08.2025", "11:30", "Operación de cadera", 3, True],
        [3, 4, "16.08.2025", "10:00", "Chequeo anual", 2, True],
        [4, 3, "17.08.2025", "09:00", "Vacunación triple", 3, True],
        [5, 5, "18.08.2025", "14:00", "Limpieza dental", 1, True],
        [6, 6, "19.08.2025", "15:30", "Control de peso", 3, False],
        [7, 7, "20.08.2025", "16:00", "Cirugía menor", 1, True],
        [8, 8, "21.08.2025", "10:30", "Desparasitación", 3, True],
        [9, 1, "22.08.2025", "11:00", "Control post-operatorio", 1, True]
    ]

    veterinarians = [
        [1, "36485787", "Martín", "Herrera", "MN12345", "mherrera@gmail.com", "1155551111", True],
        [2, "17456321", "Camila", "Álvarez", "MN54321", "calvare@gmail.com", "1155552222", False],
        [3, "34125478", "Julián", "Duarte", "MN98765", "jdurate@gmail.com", "1155553333", True],
        [4, "28765432", "Laura", "Méndez", "MN24680", "laura.mendez@example.com", "1155554444", True],
        [5, "31234567", "Nicolás", "Romero", "MN13579", "nico.romero@example.com", "1155555555", True],
        [6, "29876543", "Olivia", "Suárez", "MN11223", "olivia.suarez@example.com", "1155556666", False],
        [7, "32654321", "Pablo", "Castillo", "MN44556", "pablo.castillo@example.com", "1155557777", True],
        [8, "27654321", "Rebeca", "Ortega", "MN77889", "rebeca.ortega@example.com", "1155558888", True]
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