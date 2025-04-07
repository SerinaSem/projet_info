from models.employe import Employe
from services.employe_service import *

# Ajouter un employé
e1 = Employe(None, "Dupont", "Emma", "emma.dupont@mail.com", 25, 1)
e2 = Employe(None, "Lemoine", "Sarah", "sarah.lemoine@mail.com", 35, 1)
e3 = Employe(None, "Semmani", "Serina", "serina.semmani@mail.com", 16, 1)
ajouter_employe(e1)
ajouter_employe(e2)
ajouter_employe(e3)

# Voir tous les employés
#employes = recuperer_tous_employes()
#for e in employes:
#    print(e)

# Modifier un employé
#employe_a_modifier = recuperer_employe_par_id(1)
#if employe_a_modifier:
#    employe_a_modifier.email = "emma.nouveau@mail.com"
#    modifier_employe(employe_a_modifier)

# Supprimer un employé
#supprimer_employe(1)
