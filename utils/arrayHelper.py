def print_array_bidimensional(header, arrays):
    """
    Prints a bidimensional array of the type [[...],[...],[...]] 
    header => Headers
    arrays => List of entities
    """
    for row in header:
        print("{:10}".format(row), end="\t")
    print()
    for row in arrays:
        for value in row:
            print("{:<10}".format(value), end="\t")
        print()  
        
def print_array(header, array):
    """
    Prints a single array ["","",""]
    header => Headers
    array => List of entity values
    """
    for row in header:
        print("{:10}".format(row), end="\t")
    print()  
    for value in array:
        print("{:<10}".format(value), end="\t")
    print()  