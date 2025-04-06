from models.employe import Employe
from services.employe_service import *

# Ajouter un employé
e1 = Employe(None, "Dupont", "Emma", "emma.dupont@mail.com", 25, 1)
ajouter_employe(e1)

# Voir tous les employés
employes = recuperer_tous_employes()
for e in employes:
    print(e)

# Modifier un employé
employe_a_modifier = recuperer_employe_par_id(1)
if employe_a_modifier:
    employe_a_modifier.email = "emma.nouveau@mail.com"
    modifier_employe(employe_a_modifier)

# Supprimer un employé
supprimer_employe(1)
