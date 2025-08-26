# TP - Programación 1 - Primera Entrega

from Entities.appointments import ENCAB_TURNOS

# Encabezados
ENCAB_DUENOS = ["dueño_id", "dni", "nombre", "apellido", "email", "telefono", "activo"]
ENCAB_MASCOTAS = ["mascota_id", "nombre", "especie", "raza", "edad", "dueño_id", "peso", "sexo", "activo"]
ENCAB_VETERINARIOS = ["veterinario_id", "nombre", "apellido", "matricula", "especialidad", "telefono", "activo"]

# Función para crear las matrices con datos de prueba
def crear_matrices():
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
    veterinarios = [
        [1, "Martín", "Herrera", "MN12345", "Clínico", "+54 11 5555-1111", True],
        [2, "Camila", "Álvarez", "MN54321", "Cirujano", "+54 11 5555-2222", False],
        [3, "Julián", "Duerte", "MN98765", "Farmacéutico", "+54 11 5555-3333", True]
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
        
# Entity helper function       
def calcular_id(matriz):
    return len(matriz) + 1

# Veterinarian functions
def create_veterinarian(array_veterinarians):
    veterinarian = []
    for header in ENCAB_VETERINARIOS:
        if header == "veterinario_id":
            veterinarian.append(calcular_id(array_veterinarians))
        elif header == "activo":
            veterinarian.append(True)
        else :
            input_header = input(f'Ingresa {header}: ')
            veterinarian.append(input_header)
    array_veterinarians.append(veterinarian)
    return array_veterinarians

def read_veterinarian(veterinarian_id, array_veterinarians):
    for veterinarian in array_veterinarians:
        if(veterinarian[0] == veterinarian_id):
            return veterinarian
              
def update_veterinarian(updated_veterinarian, array_veterinarians):
    current_veterinarians_id = [veterinarian[0] for veterinarian in array_veterinarians]
    if(current_veterinarians_id.count(updated_veterinarian[0])):
        updated_veterinarian_index = current_veterinarians_id.index(updated_veterinarian[0])
        for i in range(len(array_veterinarians[updated_veterinarian_index])):
            array_veterinarians[updated_veterinarian_index][i] = updated_veterinarian[i]
    return array_veterinarians[updated_veterinarian_index]
        
def delete_veterinarian(veterinarian_id, array_veterinarians):
    current_veterinarians_id = [veterinarian[0] for veterinarian in array_veterinarians]
    if(current_veterinarians_id.count(veterinarian_id)):
        deleted_veterinarian_index = current_veterinarians_id.index(veterinarian_id)
        array_veterinarians.pop(deleted_veterinarian_index)

# Programa principal
duenos, mascotas, turnos, veterinarios = crear_matrices()

print("DUEÑOS")
imprimir_matriz(ENCAB_DUENOS, duenos)
print("\nMASCOTAS")
imprimir_matriz(ENCAB_MASCOTAS, mascotas)
print("\nTURNOS")
imprimir_matriz(ENCAB_TURNOS, turnos)
print("\nVETERINARIOS")
imprimir_matriz(ENCAB_VETERINARIOS, veterinarios)
