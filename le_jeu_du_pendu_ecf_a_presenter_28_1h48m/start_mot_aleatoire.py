import sqlite3
import random

# Fonction pour créer la base de données SQLite et la table "Mots"
def creer_base_de_donnees():
    conn = sqlite3.connect("ma_base_de_donnees.db")
    cursor = conn.cursor()

    # Création de la table "Mots"
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Mots (
            id INTEGER PRIMARY KEY,
            mot TEXT NOT NULL
        )
    """)

    # Exemple d'insertion de mots dans la table
    mots_exemples = ['python', 'javascript', 'php', 'java', 'csharp', 'html', 'css', 'ruby', 'swift', 'kotlin']
    for mot in mots_exemples:
        cursor.execute("INSERT INTO Mots (mot) VALUES (?)", (mot,))

    # Enregistrement des modifications et fermeture de la connexion
    conn.commit()
    conn.close()

# Fonction pour récupérer un mot au hasard de la table "Mots"
def mot_aleatoire():
    conn = sqlite3.connect("ma_base_de_donnees.db")
    cursor = conn.cursor()

    cursor.execute("SELECT mot FROM Mots ORDER BY RANDOM() LIMIT 1")
    mot_aleatoire = cursor.fetchone()

    conn.close()
    return mot_aleatoire[0] if mot_aleatoire else None

# Créer la base de données et la table si elles n'existent pas déjà
creer_base_de_donnees()

# Obtenir un mot au hasard de la table "Mots"
mot_a_deviner = mot_aleatoire()
if mot_a_deviner:
    print("Mot aléatoire à deviner:", mot_a_deviner)
else:
    print("Aucun mot disponible.")
