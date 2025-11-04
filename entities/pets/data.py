from utils.constants import HEADER_PET
from utils.entitiesHelper import get_next_id_by_file
from utils.filesHelper import append_line_to_file, read_file_csv_with
file_name = "./data/pets.txt"

def pet_read_handler(entity, condition):
    if condition(entity):
        return entity
    else:
        return False

def get_data_pet_by_id(_id):
    return read_file_csv_with(file_name, pet_read_handler, lambda p: p[HEADER_PET.index("pet_id")] == _id 
                                                                    and bool(p[HEADER_PET.index("active")]) == True)

def get_data_pet_by_owner_id(_owner_id):
    return read_file_csv_with(file_name, pet_read_handler, lambda p: p[HEADER_PET.index("owner_id")] == _owner_id 
                                                                    and bool(p[HEADER_PET.index("active")]) == True)

def get_data_pet_by_owner_id_and_pet_name(_owner_id, _pet_name):
    return read_file_csv_with(file_name, pet_read_handler, lambda p: p[HEADER_PET.index("owner_id")] == _owner_id 
                                                                    and bool(p[HEADER_PET.index("active")]) == True 
                                                                    and p[HEADER_PET.index("nombre") == _pet_name])

def get_data_pet_by_name(_name):
    return read_file_csv_with(file_name, pet_read_handler, lambda p: p[HEADER_PET.index("nombre")] == _name 
                                                                    and bool(p[HEADER_PET.index("active")]) == True)

def get_next_pet_id():
    return get_next_id_by_file(file_name)

def pet_append_handler(entity):
    pet_id, nombre, tipo, raza, edad, owner_id, peso, sexo, active = entity
    return f'{pet_id},{nombre},{tipo},{raza},{edad},{owner_id},{peso},{sexo},{active}'

def save_data_pet(new_pet):
    return append_line_to_file(file_name, pet_append_handler, new_pet)
