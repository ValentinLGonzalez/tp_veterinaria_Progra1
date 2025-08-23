# TP - Programación 1 - Primera Entrega

import random

# Encabezados
ENCAB_DUENOS = ["dueño_id", "dni", "nombre", "apellido", "email", "telefono", "activo"]
ENCAB_MASCOTAS = ["mascota_id", "nombre", "especie", "raza", "edad", "dueño_id", "peso", "sexo", "activo"]
ENCAB_TURNOS = ["turno_id", "mascota_id", "fecha", "hora", "tratamiento", "veterinario_id", "activo"]
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

# Appointment functions
def create_appointment(array_appointments, array_pets, array_veterinarians, array_owners):
    appointment = []
    
    for header in ENCAB_TURNOS:
        if header == "turno_id":
            appointment.append(calcular_id(array_appointments))
        elif header == "activo":
            appointment.append(True)
        elif header == "mascota_id":
            # Search for the pet by it's name and owner's DNI
            owner_found = None
            pet_found = None
            while owner_found is None:
                # Search for the owner by it's DNI
                owner_dni = input("Ingrese el DNI del dueño: ")
                for owner in array_owners:
                    if owner[1] == owner_dni and owner[6]:  
                        owner_found = owner
                        break
                
                if not owner_found:
                    print("Error: No se encontró un dueño con ese DNI") # Proximamente esto llevara a la creacion de un dueño
                    break

            if owner_found:
                while pet_found is None:
                    # Search for the pet by it's name
                    pet_name = input("Ingrese el nombre de la mascota: ")
                    pet_found = None
                    for pet in array_pets:
                        if (pet[1].lower() == pet_name.lower() and pet[5] == owner_found[0] and pet[8]): 
                            pet_found = pet
                            break
                        
                    if pet_found:
                        appointment.append(pet_found[0]) 
                        print(f"Mascota encontrada: {pet_found[1]} ({pet_found[2]} {pet_found[3]})")
                        break
                    else:
                        print("Error: No se encontró una mascota activa con ese nombre para ese dueño") # Proximamente esto llevara a la creacion de la mascota

        elif header == "veterinario_id":
            # Randomly assign a veterinarian
            active_veterinarians = [vet for vet in array_veterinarians if vet[6]] 
            random_veterianarian = random.choice(active_veterinarians)
            appointment.append(random_veterianarian[0])  
            
            print(f"Veterinario asignado: {random_veterianarian[1]} {random_veterianarian[2]} ({random_veterianarian[4]})")
        else:
            input_header = input(f'Ingresa {header}: ')
            appointment.append(input_header)
    
    array_appointments.append(appointment)
    return array_appointments

def read_appointment(appointment_id, array_appointments):
    for appointment in array_appointments:
        if appointment[0] == appointment_id:
            return appointment
    return None

def update_appointment(updated_appointment, array_appointments, array_pets, array_veterinarians):
    current_appointments_id = [appointment[0] for appointment in array_appointments if appointment[6]]
    if updated_appointment[0] in current_appointments_id:
        updated_appointment_index = current_appointments_id.index(updated_appointment[0])
        
        mascota_id_index = ENCAB_TURNOS.index("mascota_id")
        veterinario_id_index = ENCAB_TURNOS.index("veterinario_id")
        
        if not any(mascota[0] == updated_appointment[mascota_id_index] for mascota in array_pets):
            print(f"No existe una mascota con ese ID")
        
        if not any(veterinarian[0] == updated_appointment[veterinario_id_index] for veterinarian in array_veterinarians):
            print(f"No existe un veterinario con ese ID")
        
        for i in range(len(array_appointments[updated_appointment_index])):
            array_appointments[updated_appointment_index][i] = updated_appointment[i]
        
        return array_appointments[updated_appointment_index]
    return None

def delete_appointment(appointment_id, array_appointments):
    for appointment in array_appointments:
        if appointment[0] == appointment_id and appointment[6]:  
            appointment[6] = False  
            return appointment  
    return None  

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

#------ Testing Appointments ------------
#create_appointment(turnos, mascotas, veterinarios, duenos)
#imprimir_matriz(ENCAB_TURNOS, turnos)
# updated_appointment = [1, 3, "25-08-2025", "16:00", "Urgencia", 2, True]
# update_appointment(updated_appointment, turnos, mascotas, veterinarios)
# imprimir_matriz(ENCAB_TURNOS, turnos)  
# deleted_appointment= delete_appointment(2, turnos)
# imprimir_matriz(ENCAB_TURNOS, turnos)
# appointment = read_appointment(1, turnos)
# imprimir_matriz(ENCAB_TURNOS, [appointment])
