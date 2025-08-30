def print_array_bidimensional(header, array):
    # Header
    for row in header:
        print("{:10}".format(row), end="\t")
    print()
    # Rows
    for row in array:
        for value in row:
            print(value)
            print("{:<10}".format(value), end="\t")
        print()  
        
def print_array(header, array):
    # Header
    for row in header:
        print("{:10}".format(row), end="\t")
    print()  
    # Row
    for value in array:
        print("{:<10}".format(value), end="\t")
    print()  