# TP - Programación 1 - Primera Entrega

# Encabezados

ENCAB_DUENOS = ["dueño_id", "nombre", "apellido", "email", "telefono"]
ENCAB_MASCOTAS = ["mascota_id", "nombre", "especie", "raza", "edad", "dueño_id", "peso", "sexo"]
ENCAB_TURNOS = ["turno_id", "mascota_id", "fecha", "hora", "tratamiento"]
ENCAB_VETERINARIOS = ["veterinario_id", "nombre", "especialidad", "telefono", "activo"]

# Función para crear las matrices con datos de prueba

def crear_matrices():
    duenos = [
        [1, "Ana",   "Pérez",  "ana.perez@example.com",   "+54 11 5555-1111"],
        [2, "Bruno", "Silva",  "bruno.silva@example.com", "+54 11 5555-2222"],
        [3, "Carla", "Gómez",  "carla.gomez@example.com", "+54 11 5555-3333"]
    ]
    mascotas = [
        [101, "Milo",  "Perro", "Labrador",      5, 1, 23.5, "Macho"],
        [102, "Luna",  "Gato",  "Siamés",        3, 1,  4.2, "Hembra"],
        [103, "Rocky", "Perro", "Bulldog",       4, 2, 20.0, "Macho"],
        [104, "Nina",  "Gato",  "Común europeo", 2, 3,  3.8, "Hembra"]
    ]
    turnos = [
        [1001, 101, "15-08-2025", "10:00", "Extraccion"],
        [1002, 102, "16-08-2025", "11:30", "Operacion"],
        [1003, 103, "16-08-2025", "10:00", "Chequeo anual"],
        [1004, 104, "17-08-2025", "09:00", "Triple gatuna"]
    ]
    veterinarios = [
        [23, "Martín", "Herrera",  "Clínico",  "+54 11 5555-1111", True],
        [54, "Camila", "Álvarez",  "Cirujano", "+54 11 5555-2222", False],
        [32, "Julián", "Duerte",  "Farmacéutico", "+54 11 5555-3333", True]
    ]

    return duenos, mascotas, turnos, veterinarios


# Función para imprimir matrices

def imprimir_matriz(encabezado, matriz):
    # Encabezado
    for titulo in encabezado:
        print(titulo, end="\t")
    print()
    # Filas
    for fila in matriz:
        for valor in fila:
            print(valor, end="\t")
        print()


# Programa principal

duenos, mascotas, turnos = crear_matrices()

print("DUEÑOS")
imprimir_matriz(ENCAB_DUENOS, duenos)
print("\nMASCOTAS")
imprimir_matriz(ENCAB_MASCOTAS, mascotas)
print("\nTURNOS")
imprimir_matriz(ENCAB_TURNOS, turnos)
