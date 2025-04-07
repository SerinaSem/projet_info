from services.besoin_service import get_besoins_par_restaurant
from services.disponibilite_service import get_disponibilites_employe
from services.employe_service import recuperer_tous_employes
from services.horaire_service import ajouter_horaire
from models.horaire import Horaire

from datetime import datetime

def afficher_donnees_disponibilites_et_besoins(id_restaurant):
    print(f"\n📋 Chargement des besoins pour le restaurant {id_restaurant}...\n")

    # Besoins du resto
    besoins = get_besoins_par_restaurant(id_restaurant)
    for b in besoins:
        print(f"🧑‍🍳 Besoin : {b.jour} de {b.heure_debut} à {b.heure_fin} → {b.nb_employes} employés")

    print("\n📋 Chargement des disponibilités des employés...\n")

    # Employés du resto
    employes = [e for e in recuperer_tous_employes() if e.id_restaurant == id_restaurant]
    for e in employes:
        print(f"👤 {e.nom} {e.prenom} (ID {e.id}) - Contrat : {e.contrat_heures}h/sem")
        dispos = get_disponibilites_employe(e.id)
        for d in dispos:
            print(f"   📆 {d.jour} de {d.heure_debut} à {d.heure_fin}")


def planning_simple_pour_jour(id_restaurant: int, jour_cible: str):
    print(f"\n📆 Génération du planning pour le {jour_cible}...\n")

    besoins = [b for b in get_besoins_par_restaurant(id_restaurant) if b.jour == jour_cible]
    employes = [e for e in recuperer_tous_employes() if e.id_restaurant == id_restaurant]

    for besoin in besoins:
        nb_assignes = 0

        print(f"\n🧩 Besoin {besoin.jour} {besoin.heure_debut}-{besoin.heure_fin} (x{besoin.nb_employes})")

        for employe in employes:
            # On récupère les dispos de l'employé
            dispos = get_disponibilites_employe(employe.id)

            for dispo in dispos:
                if dispo.jour == jour_cible:
                    # On vérifie si la dispo couvre le besoin
                    if dispo.heure_debut <= besoin.heure_debut and dispo.heure_fin >= besoin.heure_fin:
                        # ✅ On peut l’assigner
                        h = Horaire(None, employe.id, jour_cible, besoin.heure_debut, besoin.heure_fin)
                        ajouter_horaire(h)
                        print(f"   ✅ {employe.nom} assigné")

                        nb_assignes += 1
                        break  # on ne prend qu’un créneau par employé

            if nb_assignes >= besoin.nb_employes:
                break  # besoin rempli