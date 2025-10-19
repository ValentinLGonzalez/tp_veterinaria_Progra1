TREATMENTS = [
    {'id': 1,'description': "Extraccion"},
    {'id': 2,'description': "Operacion"},
    {'id': 3,'description': "Chequeo anual"},
    {'id': 4,'description': "Vacunación"},
    {'id': 5,'description': "Triple gatuna"},
    {'id': 6,'description': "Guardia"},
    ]

def show_all_treatments(treatments):
    keys = treatments[0].keys()
    for k in keys:
        print("{:8}".format(k), end="\t")
    print()
    for treatment in treatments:
        print(f"{treatment['id']:<15} {treatment['description']:<10}", end="\t")
        print()
        
def is_valid_treatment(treatment_id):
    treatment_ids = [treatment['id'] for treatment in TREATMENTS]
    return treatment_id in treatment_ids

def get_treatment_description_by_id(id):
    treatment_description = None
    for treatment in TREATMENTS:
        if treatment['id'] == id:
            treatment_description = treatment['description']
    return treatment_description