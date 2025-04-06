from models.disponibilite import Disponibilite
from services.disponibilite_service import *

# Ajouter une disponibilité
d1 = Disponibilite(None, 2, "2025-04-08", "10:00", "14:00")
ajouter_disponibilite(d1)

# Lire les dispos de l'employé 2
dispos = get_disponibilites_employe(2)
for d in dispos:
    print(f"{d.jour} de {d.heure_debut} à {d.heure_fin}")

# Modifier une dispo
d_modif = dispos[0]
d_modif.heure_debut = "11:00"
d_modif.heure_fin = "15:00"
modifier_disponibilite(d_modif)

# Supprimer une dispo
supprimer_disponibilite(d_modif.id)
