import sqlite3
from models.disponibilite import Disponibilite

DB_PATH = "planning_resto.db"

# 🔹 Ajouter une disponibilité
def ajouter_disponibilite(dispo: Disponibilite):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO disponibilite (id_employe, jour, heure_debut, heure_fin)
        VALUES (?, ?, ?, ?)
    """, (dispo.id_employe, dispo.jour, dispo.heure_debut, dispo.heure_fin))
    conn.commit()
    conn.close()
    print(f"✅ Disponibilité ajoutée pour l'employé ID {dispo.id_employe}")

# 🔹 Récupérer les disponibilités d’un employé
def get_disponibilites_employe(id_employe):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM disponibilite WHERE id_employe = ?
    """, (id_employe,))
    rows = cursor.fetchall()
    conn.close()
    return [Disponibilite(*row) for row in rows]

# 🔹 Supprimer une disponibilité par ID
def supprimer_disponibilite(id_dispo):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM disponibilite WHERE id = ?", (id_dispo,))
    conn.commit()
    conn.close()
    print(f"🗑️ Disponibilité ID {id_dispo} supprimée.")

# (Optionnel) 🔹 Modifier une disponibilité
def modifier_disponibilite(dispo: Disponibilite):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE disponibilite
        SET jour = ?, heure_debut = ?, heure_fin = ?
        WHERE id = ?
    """, (dispo.jour, dispo.heure_debut, dispo.heure_fin, dispo.id))
    conn.commit()
    conn.close()
    print(f"✏️ Disponibilité ID {dispo.id} modifiée.")
