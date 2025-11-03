from entities.treatments.data import get_all_treatments


def is_valid_treatment(treatment_id):
    treatments = get_all_treatments()
    treatment_ids = [treatment['id'] for treatment in treatments]
    return treatment_id in treatment_ids