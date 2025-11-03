from utils.constants import HEADER_PET
from utils.entitiesHelper import get_next_id_by_file
from utils.filesHelper import append_line_to_file, read_file_csv_with
file_name = "./data/pets.txt"

def pet_read_handler(entity, condition):
    if condition(entity):
        return entity

def get_data_pet_by_id(_id):
    return read_file_csv_with(file_name, pet_read_handler, lambda p: p[HEADER_PET.index("id")] == _id and p[HEADER_PET.index("activo")] == True)

def get_data_pet_by_name(_name):
    return read_file_csv_with(file_name, pet_read_handler, lambda p: p[HEADER_PET.index("nombre")] == _name and p[HEADER_PET.index("activo")] == True)

def get_next_pet_id():
    return get_next_id_by_file(file_name)

def pet_append_handler(entity):
    pet_id, nombre, tipo, raza, edad, owner_id, peso, sexo, activo = entity
    return f'{pet_id},{nombre},{tipo},{raza},{edad},{owner_id},{peso},{sexo},{activo}'

def save_data_pet(new_pet):
    return append_line_to_file(file_name, pet_append_handler, new_pet)
