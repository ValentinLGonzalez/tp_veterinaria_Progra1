from utils.constants import HEADER_VETERINARIAN
from utils.entitiesHelper import get_next_id_by_file
from utils.filesHelper import append_line_to_file, read_all_file_csv, read_file_csv_with, update_file_csv_with_temp
file_name = "./data/veterinarians.txt"

def veterinarian_read_handler(entity, condition):
    if condition(entity):
        return entity
    else:
        return False
    
def get_data_veterinarian_by_dni(_dni):
    return read_file_csv_with(file_name, veterinarian_read_handler, lambda v: v[HEADER_VETERINARIAN.index("dni")] == _dni and bool(v[HEADER_VETERINARIAN.index("active")]) == True)

def get_data_veterinarian_by_id(_id):
    return read_file_csv_with(file_name, veterinarian_read_handler, lambda v: v[HEADER_VETERINARIAN.index("veterinarian_id")] == _id and bool(v[HEADER_VETERINARIAN.index("active")]) == True)

def get_next_veterinarian_id():
    return get_next_id_by_file(file_name)

def get_all_veterinarians_with():
    return read_all_file_csv(file_name) 

def veterinarian_append_handler(entity):
    veterinarian_id, dni, nombre, apellido, matricula, email, telefono, active = entity
    return f'{veterinarian_id},{dni},{nombre},{apellido},{matricula},{email},{telefono},{active}'

def save_data_veterinarian(new_veterinarian):
    return append_line_to_file(file_name, veterinarian_append_handler, new_veterinarian)

def update_data_veterinarian(updated_veterinarian):
    _id = updated_veterinarian[HEADER_VETERINARIAN.index("veterinarian_id")]
    update_file_csv_with_temp(file_name, lambda v: v[HEADER_VETERINARIAN.index("veterinarian_id")] == _id and bool(v[HEADER_VETERINARIAN.index("active")]) == True, updated_veterinarian)
    return updated_veterinarian

def delete_data_veterinarian(updated_veterinarian):
    _id = updated_veterinarian[HEADER_VETERINARIAN.index("veterinarian_id")]
    update_file_csv_with_temp(file_name, lambda v: v[HEADER_VETERINARIAN.index("veterinarian_id")] == _id, updated_veterinarian)
    return updated_veterinarian
