from utils.constants import HEADER_VETERINARIAN
file_name = "./data/veterinrians.txt"

def get_data_veterinarian_by_dni(_dni):
    return read_file_with(file_name, veterinarian_handler, lambda v: v.dni == _dni)
    

def veterinarian_handler(entity, condition):
    dni = entity[HEADER_VETERINARIAN.index("dni")]
    if condition(dni):
        return entity
        
def read_file_with(file_name, handler, condition):
    entity_founded = False
    try:
        with open(file_name,"r", encoding="UTF-8") as file:
            row = file.readline()
            while row and entity_founded == False:
                entity_row = row.strip().split(";")
                entity_founded = handler(entity_row, condition)
                row = file.readline()
        return entity_founded
    except OSError:
        print("No se puede abrir le archivo")