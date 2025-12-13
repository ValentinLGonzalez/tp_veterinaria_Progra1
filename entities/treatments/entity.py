from entities.treatments.data import get_all_treatments

def show_all_treatments():
    treatments = get_all_treatments()
    keys = treatments[0].keys()
    for k in keys:
        print("{:8}".format(k), end="\t")
    print()
    for treatment in treatments:
        print(f"{treatment['id']:<15} {treatment['description']:<10}", end="\t")
        print()

def get_treatment_description_by_id(id):
    treatment_description = None
    treatments = get_all_treatments()
    for treatment in treatments:
        if treatment['id'] == int(id):
            treatment_description = treatment['description']
    return treatment_description