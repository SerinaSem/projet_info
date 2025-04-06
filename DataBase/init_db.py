import sqlite3

# Connexion ou création de la base locale
conn = sqlite3.connect("planning_resto.db")
cursor = conn.cursor()

# Création des tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS restaurant (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    adresse TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS employe (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    email TEXT,
    contrat_heures INTEGER NOT NULL,
    id_restaurant INTEGER,
    FOREIGN KEY (id_restaurant) REFERENCES restaurant(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS disponibilite (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_employe INTEGER,
    jour TEXT,
    heure_debut TEXT,
    heure_fin TEXT,
    FOREIGN KEY (id_employe) REFERENCES employe(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS besoin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_restaurant INTEGER,
    jour TEXT,
    heure_debut TEXT,
    heure_fin TEXT,
    nb_employes INTEGER,
    FOREIGN KEY (id_restaurant) REFERENCES restaurant(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS horaire (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_employe INTEGER,
    jour TEXT,
    heure_debut TEXT,
    heure_fin TEXT,
    FOREIGN KEY (id_employe) REFERENCES employe(id)
)
""")

# Sauvegarder les changements
conn.commit()
conn.close()

print("✅ Base de données SQLite initialisée avec succès.")
