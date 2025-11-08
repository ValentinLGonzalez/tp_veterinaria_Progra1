import json
import os

DIVIDER_CSV = ','

def read_file_csv_with(file_name, handler, condition):
    entity_founded = False
    try:
        with open(file_name,"r", encoding="UTF-8") as file:
            row = file.readline()
            while row and entity_founded == False:
                entity_row = row.strip().split(DIVIDER_CSV)
                entity_founded = handler(entity_row, condition)
                row = file.readline()
        return entity_founded
    except OSError:
        print("No se puede abrir el archivo")

def read_last_line_with(file_name):
    last_id = 1
    try:
        with open(file_name,"r", encoding="UTF-8") as file:
            for row in file:
                row = row.strip().split(",")
                last_id = row[0]
        return last_id
    except FileNotFoundError:
        pass
    except OSError:
        print("No se puede abrir el archivo")
        
def write_file_csv(file_name, data, divider):
    try:
        file = open(file_name, "w", encoding = "UTF-8")
        for row in data:
            file.write(row.join(divider) + '\n')
    except OSError:
        print("No se puede abrir el archivo")
    finally:
        file.close()
        
def append_line_to_file(file_name, handler, data):
    try:
        file = open(file_name, "a", encoding = "UTF-8")
        file.write(handler(data) + '\n')
        return True
    except OSError:
        print("No se puede abrir el archivo")
    finally:
        file.close()

def update_file_csv_with_temp(file_name, condition, data):
    file_temp_name = "./data/temp"
    updated_success = False
    try:
        temp_file = open(file_temp_name, 'wt', encoding="UTF-8")
        current_file = open(file_name, 'rt', encoding="UTF-8")
        for rows in current_file:
            row = rows.strip().split(DIVIDER_CSV)
            if condition(row):
                temp_file.write(DIVIDER_CSV.join(data) + '\n')
            else:
                temp_file.write(DIVIDER_CSV.join(row) + '\n')
        updated_success = True
    except OSError as e:
        print("No se puede abrir el archivo")
        print(e)
    finally:
        try:
            temp_file.close()
            current_file.close()
        except:
            print("Error en el cierre del archivo:")
            
    if updated_success:
        try:
            os.remove(file_name)
            os.rename(file_temp_name, file_name)
        except OSError as error:
            print("Error al reemplazar el archivo:", error)
    else:
        os.remove(file_temp_name)
        print(f"No se pudo actualizar el archivo.")
        
def read_all_file_csv(file_name):
    try:
        data = []
        with open(file_name,"r", encoding="UTF-8") as file:
            data = read_file_recursively(file, data)
        return data
    except FileNotFoundError:
        return []
    except OSError:
        print("No se puede abrir el archivo")
        
def read_file_recursively(file, data):
    row = file.readline()
    if row:
        process_row = row.strip().split(DIVIDER_CSV)
        data.append(process_row)
        return read_file_recursively(file, data)
    else:
        return data
    
def save_all_to_file(file_name, handler, data):
    try:
        with open(file_name, "w", encoding = "UTF-8") as file:
            for row in data:
                file.write(handler(row) + '\n')
    except OSError:
        print("No se puede abrir el archivo")
        
def read_all_file_json(file_name):
    try:
        with open(file_name,"r", encoding="UTF-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except OSError:
        print("No se puede abrir el archivo")