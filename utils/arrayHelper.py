def print_array_bidimensional(header, arrays):
    """
    Imprime un arran bidimensional del tipo [[...],[...],[...]] 
    header => Encabezados
    arrays => Lista de entidades
    """
    # Header
    for row in header:
        print("{:10}".format(row), end="\t")
    print()
    # Rows
    for row in arrays:
        for value in row:
            print("{:<10}".format(value), end="\t")
        print()  
        
def print_array(header, array):
    """
    Imprime un unico array ["","",""]
    header => Encabezados
    array => Lista de valores de la entidad
    """
    # Header
    for row in header:
        print("{:10}".format(row), end="\t")
    print()  
    # Row
    for value in array:
        print("{:<10}".format(value), end="\t")
    print()  