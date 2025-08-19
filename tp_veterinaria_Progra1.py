# TP - Programación 1 - Primera Entrega

# Encabezados
ENCAB_DUENOS = ["dueño_id", "dni", "nombre", "apellido", "email", "telefono", "activo"]
ENCAB_MASCOTAS = ["mascota_id", "nombre", "especie", "raza", "edad", "dueño_id", "peso", "sexo", "activo"]
ENCAB_TURNOS = ["turno_id", "mascota_id", "fecha", "hora", "veterinario_id", "tratamiento", "activo"]
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
        [1, 1, "15-08-2025", "10:00", 1, "Extraccion", True],
        [2, 2, "16-08-2025", "11:30", 3, "Operacion", True],
        [3, 4, "16-08-2025", "10:00", 2, "Chequeo anual", True],
        [4, 3, "17-08-2025", "09:00", 3, "Triple gatuna", True]
    ]
    veterinarios = [
        [1, "Martín", "Herrera", "Clínico", "+54 11 5555-1111", True],
        [2, "Camila", "Álvarez", "Cirujano", "+54 11 5555-2222", False],
        [3, "Julián", "Duerte", "Farmacéutico", "+54 11 5555-3333", True]
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
        
def calcular_id(matriz):
    return len(matriz) + 1

def create_veterinarian(matriz_veterinarios):
    veterinarian = []
    for header in ENCAB_VETERINARIOS:
        if header == "veterinario_id":
            veterinarian.append(calcular_id(matriz_veterinarios))
        elif header == "activo":
            veterinarian.append(True)
        else :
            input_header = input(f'Ingresa {header}')
            veterinarios.append(input_header)
            
    matriz_veterinarios.append(veterinarian)
    
    return matriz_veterinarios

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

create_veterinarian(veterinarios)

print("\nVETERINARIOS")
imprimir_matriz(ENCAB_VETERINARIOS, veterinarios)