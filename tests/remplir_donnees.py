import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import random
from datetime import datetime, timedelta

from models.employe import Employe
from models.disponibilite import Disponibilite
from models.besoin import Besoin
from models.restaurant import Restaurant

from services.employe_service import ajouter_employe
from services.disponibilite_service import ajouter_disponibilites_semaine, ajouter_dispos_personnalisees, ajouter_disponibilite
from services.besoin_service import ajouter_besoin



# ----- Employés manuels -----
employes = [
    ("Durand", "Emma", "emma.durand@mail.com", 25),
    ("Morel", "Lucas", "lucas.morel@mail.com", 30),
    ("Bernard", "Sophie", "sophie.bernard@mail.com", 35),
    ("Lemoine", "Alex", "alex.lemoine@mail.com", 20),
    ("Gomez", "Lea", "lea.gomez@mail.com", 25),
    ("Nguyen", "Hugo", "hugo.nguyen@mail.com", 35),
    ("Rossi", "Chloe", "chloe.rossi@mail.com", 30),
    ("Klein", "Tom", "tom.klein@mail.com", 20)
]

for nom, prenom, email, contrat in employes:
    ajouter_employe(Employe(None, nom, prenom, email, contrat, 1))

# ----- Dispos des 8 employés -----
ajouter_disponibilites_semaine(1, "07:00", "15:00")
ajouter_dispos_personnalisees(2, {
    "Lundi": ("11:00", "19:00"),
    "Mercredi": ("06:00", "14:00"),
    "Samedi": ("10:00", "18:00")
})
ajouter_disponibilites_semaine(3, "05:00", "13:00")
ajouter_disponibilites_semaine(4, "12:00", "20:00")
ajouter_disponibilites_semaine(5, "08:00", "16:00")
ajouter_dispos_personnalisees(6, {
    "Mardi": ("10:00", "18:00"),
    "Jeudi": ("11:00", "15:00"),
    "Dimanche": ("14:00", "22:00")
})
ajouter_disponibilites_semaine(7, "09:00", "17:00")
ajouter_disponibilites_semaine(8, "18:00", "00:00")

# ----- Employés générés automatiquement (42) -----
noms = ["Martin", "Bernard", "Thomas", "Petit", "Robert", "Richard", "Durand", "Dubois", "Moreau", "Laurent"]
prenoms = ["Emma", "Louis", "Jade", "Hugo", "Louise", "Gabriel", "Alice", "Leo", "Chloe", "Raphael"]
jours_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

for i in range(42):
    nom = random.choice(noms)
    prenom = random.choice(prenoms)
    email = f"{prenom.lower()}.{nom.lower()}{random.randint(1,999)}@mail.com"
    contrat = random.choice([20, 25, 30, 35])
    ajouter_employe(Employe(None, nom, prenom, email, contrat, 1))

# ----- Disponibilités des 50 employés -----
def generer_dispos():
    for id_employe in range(1, 51):  # 8 manuels + 42 générés = 50
        jours_dispo = random.sample(jours_semaine, k=random.randint(3, 5))
        for jour in jours_dispo:
            nb_creneaux = random.choice([1, 2])
            heures_dispos = []

            if nb_creneaux == 1:
                debut = random.choice(["05:00", "08:00", "10:00", "13:00", "16:00"])
                fin = (datetime.strptime(debut, "%H:%M") + timedelta(hours=random.randint(4, 8))).strftime("%H:%M")
                heures_dispos.append((debut, fin))
            else:
                debut1 = random.choice(["05:00", "06:00", "07:00", "08:00", "09:00"])
                fin1 = (datetime.strptime(debut1, "%H:%M") + timedelta(hours=random.randint(3, 5))).strftime("%H:%M")
                debut2 = fin1
                fin2 = (datetime.strptime(debut2, "%H:%M") + timedelta(hours=random.randint(3, 5))).strftime("%H:%M")
                heures_dispos.append((debut1, fin1))
                heures_dispos.append((debut2, fin2))

            for debut, fin in heures_dispos:
                ajouter_disponibilite(Disponibilite(None, id_employe, jour, debut, fin))

generer_dispos()

# ----- Besoins -----
jours = jours_semaine
plages = [
    ("05:00", "11:00", 6),
    ("11:00", "15:00", 10),  # Rush
    ("15:00", "18:00", 6),
    ("18:00", "21:00", 10),  # Rush
    ("21:00", "00:00", 6)
]

for jour in jours:
    for debut, fin, nb in plages:
        ajouter_besoin(Besoin(None, 1, jour, debut, fin, nb))

print("\n✅ Base remplie avec 50 employés + dispo + besoins.")
