import sqlite3
from models.horaire import Horaire

DB_PATH = "planning_resto.db"

# 🔹 Ajouter un horaire
def ajouter_horaire(horaire: Horaire):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO horaire (id_employe, jour, heure_debut, heure_fin)
        VALUES (?, ?, ?, ?)
    """, (horaire.id_employe, horaire.jour, horaire.heure_debut, horaire.heure_fin))
    conn.commit()
    conn.close()
    print(f"✅ Horaire ajouté pour l'employé ID {horaire.id_employe}")

# 🔹 Récupérer les horaires d’un employé
def get_horaires_employe(id_employe):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM horaire WHERE id_employe = ?
    """, (id_employe,))
    rows = cursor.fetchall()
    conn.close()
    return [Horaire(*row) for row in rows]

# 🔹 Récupérer tous les horaires (optionnel)
def get_tous_les_horaires():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM horaire")
    rows = cursor.fetchall()
    conn.close()
    return [Horaire(*row) for row in rows]

# 🔹 Supprimer un horaire par ID
def supprimer_horaire(id_horaire):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM horaire WHERE id = ?", (id_horaire,))
    conn.commit()
    conn.close()
    print(f"🗑️ Horaire ID {id_horaire} supprimé.")

# (Optionnel) 🔹 Modifier un horaire
def modifier_horaire(horaire: Horaire):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE horaire
        SET jour = ?, heure_debut = ?, heure_fin = ?
        WHERE id = ?
    """, (horaire.jour, horaire.heure_debut, horaire.heure_fin, horaire.id))
    conn.commit()
    conn.close()
    print(f"✏️ Horaire ID {horaire.id} modifié.")
