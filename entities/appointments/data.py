from utils.constants import HEADER_APPOINTMENT
from utils.entitiesHelper import get_next_id_by_file
from utils.filesHelper import append_line_to_file, read_all_file_csv, read_file_csv_with, update_file_csv_with_temp
file_name = "./data/appointments.txt"

def appointment_read_handler(entity, condition):
    """
    Handler function used to filter appointments based on a condition.

    """
    if condition(entity):
        return entity
    else:
        False
    
def get_data_appointment_by_id(_id):
    """
    Retrieves an active appointment by its ID.

    """
    return read_file_csv_with(file_name, appointment_read_handler, lambda a: a[HEADER_APPOINTMENT.index("appointment_id")] == _id and bool(a[HEADER_APPOINTMENT.index("active")]) == True)

def get_next_appointment_id():
    """
    Retrieves the next available appointment ID.

    """
    return get_next_id_by_file(file_name)

def get_all_appointments_with():
    """
    Returns all appointments from file.

    """
    return read_all_file_csv(file_name) 

def get_data_appointment_by_pet_and_vet(pet_id, veterinarian_id):
    """
    Retrieves an active appointment by pet ID and veterinarian ID.

    """
    return read_file_csv_with(file_name, appointment_read_handler, 
        lambda a: (a[HEADER_APPOINTMENT.index("pet_id")] == pet_id and 
                  a[HEADER_APPOINTMENT.index("veterinarian_id")] == veterinarian_id and 
                  bool(a[HEADER_APPOINTMENT.index("active")]) == True)
    )

def appointment_append_handler(entity):
    """
    Converts an appointment entity to CSV line format.

    """
    appointment_id, pet_id, fecha, hora, treatment_id, veterinarian_id, active = entity
    return f'{appointment_id},{pet_id},{fecha},{hora},{treatment_id},{veterinarian_id},{active}'

def save_data_appointment(new_appointment):
    """
    Appends a new appointment to the file.

    """
    return append_line_to_file(file_name, appointment_append_handler, new_appointment)

def update_data_appointment(updated_appointment):
    """
    Updates an existing appointment in the file.

    """
    _id = updated_appointment[HEADER_APPOINTMENT.index("appointment_id")]
    update_file_csv_with_temp(file_name, lambda v: v[HEADER_APPOINTMENT.index("appointment_id")] == _id and bool(v[HEADER_APPOINTMENT.index("active")]) == True, updated_appointment)
    return updated_appointment

def delete_data_appointment(updated_appointment):
    """
    Deletes (soft delete) an appointment by ID.

    """
    _id = updated_appointment[HEADER_APPOINTMENT.index("appointment_id")]
    update_file_csv_with_temp(file_name, lambda v: v[HEADER_APPOINTMENT.index("appointmen_id")] == _id, updated_appointment)
    return updated_appointment
