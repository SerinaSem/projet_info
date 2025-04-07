import sqlite3

DB_PATH = "planning_resto.db"

tables = ["horaire", "besoin", "disponibilite", "employe", "restaurant"]

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

for table in tables:
    cursor.execute(f"DELETE FROM {table}")
    cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{table}'")  # remet l'auto-increment à 1
    print(f"🗑️ Table {table} vidée.")

# Ajouter un restaurant (ID 1), sinon erreurs quand on ajoute des employés
cursor.execute("INSERT INTO restaurant (nom, adresse) VALUES (?, ?)", ("La Perle du Vieux Port", "Marseille"))
print("🏪 Restaurant ajouté.")

conn.commit()
conn.close()

print("\n✅ Réinitialisation terminée.")
