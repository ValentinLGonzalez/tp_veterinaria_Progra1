from Utils.arrayHelper import imprimir_matriz
from Utils.constants import ENCAB_VETERINARIOS

# Entity helper function       
def calcular_id(matriz):
    return len(matriz) + 1
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
        
def show_veterinarians(array_veterinarians): 
    imprimir_matriz(ENCAB_VETERINARIOS, array_veterinarians)