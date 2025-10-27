def read_file_csv_with(file_name, handler, condition):
    entity_founded = False
    try:
        with open(file_name,"r", encoding="UTF-8") as file:
            row = file.readline()
            while row and entity_founded == False:
                entity_row = row.strip().split(",")
                entity_founded = handler(entity_row, condition)
                row = file.readline()
        return entity_founded
    except OSError:
        print("No se puede abrir le archivo")

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
        print("No se puede abrir le archivo")
        
def write_file(file_name, data, divider):
    try:
        file = open(file_name, "w", encoding = "UTF-8")
        for row in data:
            file.write(row.join(divider) + '\n')
    except OSError:
        print("No se puede abrir le archivo")
    finally:
        file.close()
        
def append_line_to_file(file_name, handler, data):
    try:
        file = open(file_name, "a", encoding = "UTF-8")
        file.write(handler(data) + '\n')
        return True
    except OSError:
        print("No se puede abrir le archivo")
    finally:
        file.close()

def read_all_file_csv(file_name):
    data = []
    try:
        with open(file_name,"r", encoding="UTF-8") as file:
            for row in file:
                entity_row = row.strip().split(",")
                data.append(entity_row)
        return data
    except FileNotFoundError:
        return []
    except OSError:
        print("No se puede abrir le archivo")

def save_all_to_file(file_name, handler, data):
    try:
        with open(file_name, "w", encoding = "UTF-8") as file:
            for row in data:
                file.write(handler(row) + '\n')
    except OSError:
        print("No se puede abrir le archivo")