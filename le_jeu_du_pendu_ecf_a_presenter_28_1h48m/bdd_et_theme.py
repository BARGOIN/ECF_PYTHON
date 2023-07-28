import tkinter as tk
from tkinter import ttk
import sqlite3
import random
def fmenu():
 

    # Fonction pour créer la base de données SQLite et les tables
    def creer_base_de_donnees():
        conn = sqlite3.connect("ma_base_de_donnees.db")
        cursor = conn.cursor()

        # Création de la table "Theme"
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Theme (
                id INTEGER PRIMARY KEY,
                nom TEXT NOT NULL
            )
        """)

        # Création de la table "Mot"
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Mot (
                id INTEGER PRIMARY KEY,
                mot TEXT NOT NULL,
                theme_id INTEGER NOT NULL,
                FOREIGN KEY (theme_id) REFERENCES Theme(id)
            )
        """)

        # Exemple d'ajout de thèmes et de mots  
        themes = ["developpeur", "designer", "linux"]
        mots = {
            "developpeur": ["python", "php", "js", "code"],
            "designer": ["ui", "figma", "pixabay"],
            "linux": ["sudo", "install", "tux", "noyeau"]
        }

        for theme in themes:
            cursor.execute("INSERT INTO Theme (nom) VALUES (?)", (theme,))
            theme_id = cursor.lastrowid
            for mot in mots[theme]:
                cursor.execute("INSERT INTO Mot (mot, theme_id) VALUES (?, ?)", (mot, theme_id))

        # Enregistrement des modifications et fermeture de la connexion
        conn.commit()
        conn.close()

    # Fonction pour récupérer un mot au hasard d'un thème donné
    def mot_aleatoire_par_theme(theme):
        conn = sqlite3.connect("ma_base_de_donnees.db")
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM Theme WHERE nom = ?", (theme,))
        theme_id = cursor.fetchone()

        if not theme_id:
            conn.close()
            return None

        cursor.execute("SELECT mot FROM Mot WHERE theme_id = ?", (theme_id[0],))
        mots = cursor.fetchall()
        mot_aleatoire = random.choice(mots)[0]

        conn.close()
        return mot_aleatoire

    # Créer la base de données et les tables si elles n'existent pas déjà
    creer_base_de_donnees()

    # Création de la fenêtre principale
    fenetre = tk.Tk()
    fenetre.title("Générateur de mots aléatoires")

    # Fonction pour gérer l'action du bouton
    def obtenir_mot_aleatoire():
        theme = theme_combobox.get()
        mot_aleatoire = mot_aleatoire_par_theme(theme)
        if mot_aleatoire:
            resultat_label.config(text=f"Mot aléatoire du thème '{theme}': {mot_aleatoire}")
            
        else:
            resultat_label.config(text="Thème introuvable.")
            # ================================================================================
        
    # Création des widgets
    theme_label = tk.Label(fenetre, text="Choisir un thème:")
    theme_label.pack(pady=5)

    # Récupérer tous les thèmes depuis la base de données
    conn = sqlite3.connect("ma_base_de_donnees.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nom FROM Theme")
    themes = cursor.fetchall()
    conn.close()
    themes = [theme[0] for theme in themes]

    theme_combobox = ttk.Combobox(fenetre, values=themes, width=30)
    theme_combobox.pack(pady=5)
    theme_combobox.set(themes[0])  # Sélectionner le premier thème par défaut

    bouton_generer = ttk.Button(fenetre, text="Générer un mot aléatoire", command=obtenir_mot_aleatoire)
    bouton_generer.pack(pady=5)

    resultat_label = tk.Label(fenetre, text="", font=("Helvetica", 12))
    resultat_label.pack(pady=10)



    # Lancement de la boucle principale de la fenêtre
    fenetre.mainloop()