import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('./instance/budget.db')
cursor = conn.cursor()

# Suppression des lignes
cursor.execute("DELETE FROM expense WHERE id IN (3, 4)")
conn.commit()

print("Les lignes ont été supprimées avec succès.")

# Fermeture de la connexion
conn.close()

