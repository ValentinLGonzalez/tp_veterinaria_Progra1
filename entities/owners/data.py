from utils.constants import HEADER_OWNER
from utils.entitiesHelper import get_next_id_by_file
from utils.filesHelper import append_line_to_file, read_file_csv_with, save_all_to_file, read_all_file_csv

file_name = "./data/owners.txt"

def owner_read_handler(entity, condition):
    if condition(entity):
        return entity

def get_data_owner_by_dni(_dni):
    return read_file_csv_with(file_name, owner_read_handler, lambda o: o[HEADER_OWNER.index("dni")] == _dni and o[HEADER_OWNER.index("active")] == "True")

def get_data_owner_by_id(_id):
    return read_file_csv_with(file_name, owner_read_handler, lambda o: o[HEADER_OWNER.index("owner_id")] == _id and o[HEADER_OWNER.index("active")] == "True")

def get_next_owner_id():
    return get_next_id_by_file(file_name)

def owner_append_handler(entity):
    owner_id, dni, nombre, apellido, email, telefono, active = entity
    return f'{owner_id},{dni},{nombre},{apellido},{email},{telefono},{active}'

def save_data_owner(new_owner):
    return append_line_to_file(file_name, owner_append_handler, new_owner)

def get_all_owners():
    return read_all_file_csv(file_name)

def save_all_owners(owners):
    return save_all_to_file(file_name, owner_append_handler, owners)
