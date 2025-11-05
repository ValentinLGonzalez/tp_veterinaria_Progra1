from utils.constants import HEADER_PET
from utils.entitiesHelper import get_next_id_by_file
from utils.filesHelper import append_line_to_file, read_all_file_csv, read_file_csv_with, update_file_csv_with_temp
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

def get_all_pets():
    return read_all_file_csv(file_name)

def update_data_pets(updated_pet):
    id = updated_pet[HEADER_PET.index("pet_id")]
    update_file_csv_with_temp(file_name, lambda v: v[HEADER_PET.index("pet_id")] == id and bool(v[HEADER_PET.index("active")]) == True, updated_pet)
    return updated_pet

def delete_data_pets(deleted_pet):
    id = deleted_pet[HEADER_PET.index("pet_id")]
    update_file_csv_with_temp(file_name, lambda v: v[HEADER_PET.index("pet_id")] == id, deleted_pet)
    return deleted_pet