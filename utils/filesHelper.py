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