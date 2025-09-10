# Entity helper function       
from utils.constants import EXCLUDED_PRINT_HEADERS


def get_next_id(matriz):
    return len(matriz) + 1

# Función para crear las matrices con datos de prueba
def create_arrays():
    owners = [
        [1, "35125487", "Ana", "Pérez", "ana.perez@example.com", "1144441111", True],
        [2, "45785126", "Bruno", "Silva", "bruno.silva@example.com", "1144442222", True],
        [3, "52654789", "Carla", "Gómez", "carla.gomez@example.com", "1144443333", True]
    ]
    mascotas = [
        [1, "Milo", "Perro", "Labrador", 5, 1, 23.5, "Macho", True],
        [2, "Luna", "Gato", "Siamés", 3, 1, 4.2, "Hembra", True],
        [3, "Rocky", "Perro", "Bulldog", 4, 2, 20.0, "Macho", True],
        [4, "Nina", "Gato", "Común europeo", 2, 3, 3.8, "Hembra", True]
    ]
    turnos = [
        [1, 1, "15-08-2025", "10:00", "Extraccion", 1, True],
        [2, 2, "16-08-2025", "11:30", "Operacion", 3, True],
        [3, 4, "16-08-2025", "10:00", "Chequeo anual", 2, True],
        [4, 3, "17-08-2025", "09:00", "Triple gatuna", 3, True]
    ]
    veterinarians = [
        [1, "36485787", "Martín", "Herrera", "MN12345", "mherrera@gmail.com", "1155551111", True],
        [2, "17456321", "Camila", "Álvarez", "MN54321", "calvare@gmail.com", "1155552222", False],
        [3, "34125478", "Julián", "Duarte", "MN98765", "jdurate@gmail.com", "1155553333", True]
    ]

    return owners, mascotas, turnos, veterinarians

def update_entity_data(entity, headers):
    updated_entity = entity.copy()
    for header in headers:
        if header in EXCLUDED_PRINT_HEADERS:
            continue
        index = headers.index(header)
        input_header = input(f'Ingresa {header}: ')
        updated_entity[index] = input_header 
    return updated_entity