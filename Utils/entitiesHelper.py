# Entity helper function       
def calculate_id(matriz):
    return len(matriz) + 1

# Función para crear las matrices con datos de prueba
def create_arrays():
    duenos = [
        [1, "35125487", "Ana", "Pérez", "ana.perez@example.com", "+54 11 5555-1111", True],
        [2, "45785126", "Bruno", "Silva", "bruno.silva@example.com", "+54 11 5555-2222", True],
        [3, "52654789", "Carla", "Gómez", "carla.gomez@example.com", "+54 11 5555-3333", True]
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
        [1, "36485787", "Martín", "Herrera", "MN12345", "Clínico", "+54 11 5555-1111", True],
        [2, "17456321", "Camila", "Álvarez", "MN54321", "Cirujano", "+54 11 5555-2222", False],
        [3, "34125478", "Julián", "Duerte", "MN98765", "Farmacéutico", "+54 11 5555-3333", True]
    ]

    return duenos, mascotas, turnos, veterinarians