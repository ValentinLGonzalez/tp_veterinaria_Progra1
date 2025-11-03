from utils.filesHelper import read_all_file_json


file_name = "./data/treatments.json"

def get_all_treatments():
    return read_all_file_json(file_name)