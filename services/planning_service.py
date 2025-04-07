from services.besoin_service import get_besoins_par_restaurant
from services.disponibilite_service import get_disponibilites_employe
from services.employe_service import recuperer_tous_employes
from services.horaire_service import ajouter_horaire, get_total_heures_employe, get_horaires_employe
from models.horaire import Horaire
from datetime import datetime


def afficher_donnees_disponibilites_et_besoins(id_restaurant):
    print(f"\n📋 Chargement des besoins pour le restaurant {id_restaurant}...\n")
    besoins = get_besoins_par_restaurant(id_restaurant)
    for b in besoins:
        print(f"🧑‍🍳 Besoin : {b.jour} de {b.heure_debut} à {b.heure_fin} → {b.nb_employes} employés")

    print("\n📋 Chargement des disponibilités des employés...\n")

    employes = [e for e in recuperer_tous_employes() if e.id_restaurant == id_restaurant]
    for e in employes:
        print(f"👤 {e.nom} {e.prenom} (ID {e.id}) - Contrat : {e.contrat_heures}h/sem")
        dispos = get_disponibilites_employe(e.id)
        for d in dispos:
            print(f"   📆 {d.jour} de {d.heure_debut} à {d.heure_fin}")


def planning_simple_pour_jour(id_restaurant: int, jour_cible: str, heures_employes: dict, employes: list):
    print(f"\n📆 Génération du planning pour le {jour_cible}...\n")

    besoins = [b for b in get_besoins_par_restaurant(id_restaurant) if b.jour == jour_cible]

    for besoin in besoins:
        nb_assignes = 0
        print(f"\n🧩 Besoin {besoin.jour} {besoin.heure_debut}-{besoin.heure_fin} (x{besoin.nb_employes})")

        for employe in employes:
            heures_assignées = heures_employes[employe.id]

            if heures_assignées >= employe.contrat_heures:
                print(f"   ❌ {employe.nom} déjà au max ({heures_assignées:.1f}h / {employe.contrat_heures}h)")
                continue

            dispos = get_disponibilites_employe(employe.id)

            for dispo in dispos:
                if dispo.jour == jour_cible:
                    if dispo.heure_debut <= besoin.heure_debut and dispo.heure_fin >= besoin.heure_fin:
                        debut_besoin = datetime.strptime(besoin.heure_debut, "%H:%M")
                        fin_besoin = datetime.strptime(besoin.heure_fin, "%H:%M")
                        duree_besoin = (fin_besoin - debut_besoin).total_seconds() / 3600

                        if heures_assignées + duree_besoin <= employe.contrat_heures:
                            h = Horaire(None, employe.id, jour_cible, besoin.heure_debut, besoin.heure_fin)
                            ajouter_horaire(h)
                            heures_employes[employe.id] += duree_besoin

                            print(f"   ✅ {employe.nom} assigné ({heures_employes[employe.id]:.1f}h / {employe.contrat_heures}h)")
                            nb_assignes += 1
                            break
                        else:
                            print(f"   ❌ {employe.nom} dépasserait son contrat ({heures_assignées:.1f}h + {duree_besoin:.1f}h > {employe.contrat_heures}h)")

            if nb_assignes >= besoin.nb_employes:
                break


def generer_planning_semaine(id_restaurant: int):
    jours_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    employes = [e for e in recuperer_tous_employes() if e.id_restaurant == id_restaurant]
    heures_employes = initialiser_heures_employes(employes)

    for jour in jours_semaine:
        print(f"\n📆 ====== {jour.upper()} ======")
        planning_simple_pour_jour(id_restaurant, jour, heures_employes, employes)

    print("\n✅ Génération complète du planning de la semaine terminée.")


def afficher_planning_employe(id_employe: int):
    print(f"\n📅 Planning de l'employé ID {id_employe} :")
    horaires = get_horaires_employe(id_employe)

    if not horaires:
        print("Aucun horaire trouvé.")
        return

    horaires_triees = sorted(horaires, key=lambda h: h.jour)
    for h in horaires_triees:
        print(f"🕒 {h.jour} : {h.heure_debut} → {h.heure_fin}")


def initialiser_heures_employes(employes):
    return {e.id: get_total_heures_employe(e.id) for e in employes}

def afficher_total_heures_semaine(heures_employes: dict, employes: list):
    print("\n📊 Récapitulatif des heures par employé :\n")
    for employe in employes:
        heures = heures_employes.get(employe.id, 0)
        print(f"👤 {employe.nom} {employe.prenom} → {heures:.1f}h / {employe.contrat_heures}h")
