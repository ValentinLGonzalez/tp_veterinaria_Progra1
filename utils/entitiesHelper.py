# Entity helper function       
from utils.filesHelper import read_last_line_with

def get_next_id_by_file(file_name):
    return int(read_last_line_with(file_name)) + 1