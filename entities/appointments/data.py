from utils.constants import HEADER_APPOINTMENT
from utils.entitiesHelper import get_next_id_by_file
from utils.filesHelper import append_line_to_file, read_file_csv_with
file_name = "./data/appointments.txt"

def appointment_read_handler(entity, condition):
    if condition(entity):
        return entity
    
def get_data_appointment_by_id(_id):
    return read_file_csv_with(file_name, appointment_read_handler, lambda a: a[HEADER_APPOINTMENT.index("appointment_id")] == _id and a[HEADER_APPOINTMENT.index("active")] == "True")

def get_next_appointment_id():
    return get_next_id_by_file(file_name)

def appointment_append_handler(entity):
    appointment_id, pet_id, fecha, hora, treatment_id, veterinarian_id, active = entity
    return f'{appointment_id},{pet_id},{fecha},{hora},{treatment_id},{veterinarian_id},{active}'

def save_data_appointment(new_appointment):
    return append_line_to_file(file_name, appointment_append_handler, new_appointment)
