from Utils.arrayHelper import imprimir_matriz
from Utils.constants import ENCAB_VETERINARIOS
from Utils.entitiesHelper import calcular_id
from Utils.menuHelper import mostrar_menu

def create_veterinarian(array_veterinarians):
    new_veterinarian = []
    for header in ENCAB_VETERINARIOS:
        if header == "veterinario_id":
            new_veterinarian.append(calcular_id(array_veterinarians))
        elif header == "activo":
            new_veterinarian.append(True)
        else :
            input_header = input(f'Ingresa {header}: ')
            new_veterinarian.append(input_header)
    array_veterinarians.append(new_veterinarian)
    return new_veterinarian

def read_veterinarian_by_id(veterinarian_id, array_veterinarians):
    for veterinarian in array_veterinarians:
        if(veterinarian[0] == veterinarian_id):
            return veterinarian
              
def update_veterinarian_by_id(veterinarian_id, updated_veterinarian, array_veterinarians):
    current_veterinarians_id = [veterinarian[0] for veterinarian in array_veterinarians]
    if(current_veterinarians_id.count(veterinarian_id)):
        updated_veterinarian_index = current_veterinarians_id.index(veterinarian_id)
        for i in range(len(array_veterinarians[updated_veterinarian_index])):
            array_veterinarians[updated_veterinarian_index][i] = updated_veterinarian[i]
    return array_veterinarians[updated_veterinarian_index]
        
def delete_veterinarian_by_id(veterinarian_id, array_veterinarians):
    current_veterinarians_id = [veterinarian[0] for veterinarian in array_veterinarians]
    if(current_veterinarians_id.count(veterinarian_id)):
        deleted_veterinarian_index = current_veterinarians_id.index(veterinarian_id)
        array_veterinarians.pop(deleted_veterinarian_index)
        
def show_all_veterinarians(array_veterinarians): 
    imprimir_matriz(ENCAB_VETERINARIOS, array_veterinarians)
    
def show_veterinarian(veterinarians): 
    imprimir_matriz(ENCAB_VETERINARIOS, veterinarians)

def add_veterinarian_menu(veterinarians):
    print("Ingrese los datos del Veterinario: \n")
    new_veterinarian = create_veterinarian(veterinarians)
    show_veterinarian(new_veterinarian)
     
def show_submenu_veterinarians(veterinarians): 
    """
    Veterinarians Controller
    """
    TITLE = "Bienvenidos al menu veterinarios"
    OPTIONS = ["Agregar un Veterinario","Mostrar todos los Veterinarios", "Modificar un Veterinario por DNI", "Eliminar Veterinario por DNI"]
    ACTIONS = [ 
                add_veterinarian_menu(veterinarians),
                show_all_veterinarians(veterinarians),
                modify_veterinarian(),
                remove_veterinarian()
                ]
    mostrar_menu(TITLE, OPTIONS, ACTIONS )