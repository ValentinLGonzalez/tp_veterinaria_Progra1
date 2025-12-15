from entities.pets.data import get_all_pets
from utils.constants import HEADER_PET

def pet_statistics():
    print("\n--- Estadísticas de Mascotas ---\n")
    staditics = {"total_active_pets": 0, "total_inactive_pets": 0, "total_species": {}, "breeds_by_species": {}}
    pets = get_all_pets()

    all_pets_set = { tuple(p) for p in pets }
    active_pets = { tuple(p) for p in pets if p[HEADER_PET.index("active")] == 'True' }
    inactive_pets = all_pets_set - active_pets


    print(f"Total de mascotas activas: {len(active_pets)}\n")
    staditics["total_active_pets"] = len(active_pets)
    print(f"Total de mascotas no activas: {len(inactive_pets)}\n")
    staditics["total_inactive_pets"] = len(inactive_pets)

    species = {
        p[HEADER_PET.index("especie")].upper()
        for p in active_pets
    }

    print("Especies registradas:", species)
    staditics["total_species"] = species
    breeds_by_species = {}
    for sp in species:
        breeds_by_species[sp] = { p[HEADER_PET.index("raza")].upper() for p in active_pets if p[HEADER_PET.index("especie")].upper() == sp }

    print("Razas por especie:")
    for sp, breeds in breeds_by_species.items():
        print(f"  {sp}: {breeds}")
    print()

    staditics["breeds_by_species"] = breeds_by_species

    print("\n--- Fin de estadísticas de mascotas ---\n")
    return staditics