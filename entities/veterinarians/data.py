from utils.constants import HEADER_VETERINARIAN
from utils.filesHelper import append_line_to_file, read_file_csv_with
file_name = "./data/veterinrians.txt"

def veterinarian_read_handler(entity, condition):
    if condition(entity):
        return entity
    
def veterinarian_append_handler(entity):
    veterinarian_id, dni, nombre, apellido, matricula, email, telefono, active = entity
    return f'{veterinarian_id},{dni},{nombre},{apellido},{matricula},{email},{telefono},{active}'
    
def get_data_veterinarian_by_dni(_dni):
    return read_file_csv_with(file_name, veterinarian_read_handler, lambda v: v[HEADER_VETERINARIAN.index("dni")] == _dni and v[HEADER_VETERINARIAN.index("activo")] == True)

def get_data_veterinarian_by_id(_id):
    return read_file_csv_with(file_name, veterinarian_read_handler, lambda v: v[HEADER_VETERINARIAN.index("id")] == _id and v[HEADER_VETERINARIAN.index("activo")] == True)

def save_data_veterinarian(new_veterinarian):
    return append_line_to_file(file_name, veterinarian_append_handler, new_veterinarian)
