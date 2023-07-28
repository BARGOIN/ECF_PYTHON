from tkinter import *
import tkinter as tk
# from bdd_et_theme import fmenu
# from pendu_et_clavier import* 
from tkinter import *
from start_mot_aleatoire import*
import xml.etree.ElementTree as ET 
from tkinter import simpledialog
# =======================================================================================================
# partie pendu
# =======================================================================================================

class App( ):
    def charger_menus(self):
        try:
            tree = ET.parse("menus.xml")
            root = tree.getroot()

            for menu_element in root.findall("menu"):
                menu_name = menu_element.get("categorie")
                menu = tk.Menu(self.root)

                for lien_element in menu_element.findall("lien"):
                    label = lien_element.find("label").text
                    command_name = lien_element.find("command").text
                    command_function = getattr(self, command_name, None)
                    if command_function:
                        menu.add_command(label=label, command=command_function)

                self.root.config(menu=menu)
        except FileNotFoundError:
            print("Fichier XML de menus introuvable.")

    def __init__(self) -> None:
        self.base = ("line", 30, 190, 170, 190)
        self.mas = ("line", 70, 190, 70, 10)
        self.haut = ("line", 170, 10, 70, 10)
        self.angle = ("line", 100, 10, 70, 50)
        self.petit_bout = ("line", 170, 10, 170, 40)
        self.tete = ("oval", 155, 40, 185, 70)
        self.corps = ("line", 170, 140, 170, 70)
        self.bras = ("line", 190, 80, 150, 80)
        self.j_gauche = ("line", 170, 140, 150, 160)
        self.j_droite = ("line", 170, 140, 190, 160)
        self.trait = [self.base, self.mas, self.haut, self.angle, 
                      self.petit_bout, self.tete, self.corps, self.bras, 
                      self.j_gauche, self.j_droite]
        self.cpt = 0
         
        self.config = {
            "canevas": "ivory",
            "letters": {
                "active": "black",
                "used": "grey",
                "border": "black"
            },
            "line": {
                "color": "black",
                "width": 2
            },
            "theme": 1
        }
        self.current_theme = None

    def charger_configuration(self):
        try:
            with open("config.json", "r") as config_file:
                self.config = json.load(config_file)
        except FileNotFoundError:
            self.config = {
                "canevas": "ivory",
                "letters": {
                    "active": "black",
                    "used": "grey",
                    "border": "black"
                },
                "line": {
                    "color": "black",
                    "width": 2
                },
                "theme": 1
            }

    def tracer(self):
        self.cpt += 1

        if self.cpt < 11:
            for t in range(0,10):  
                if self.cpt == 6:
                    canevas.create_oval(self.trait[self.cpt-1][1], self.trait[self.cpt-1][2], 
                                        self.trait[self.cpt-1][3], self.trait[self.cpt-1][4], 
                                        fill="ivory", width=2)
                else:
                    canevas.create_line(self.trait[self.cpt-1][1], self.trait[self.cpt-1][2], 
                                        self.trait[self.cpt-1][3], self.trait[self.cpt-1][4], 
                                        fill="black", width=2)
        else:
            print("Perdu")
            exit()
    # ===============================================================================
    # crud du menu edition
    # ===============================================================================
    def lire_mot(self):
        # Récupérer le mot sélectionné dans le menu "Édition"
        mot_selectionne = "Mot à lire"  # Remplacez cette ligne par le code pour obtenir le mot sélectionné
        simpledialog.showinfo("Lire le mot", f"Le mot sélectionné est : {mot_selectionne}")

    def ecrire_mot(self):
        nouveau_mot = simpledialog.askstring("Nouveau mot", "Saisissez le nouveau mot :")
        if nouveau_mot:
            # Ajouter le nouveau_mot à la base de données
            # Code pour ajouter le nouveau_mot à la base de données
            simpledialog.showinfo("Succès", "Le mot a été ajouté avec succès.")

    def modifier_mot(self):
        mot_a_modifier = "Mot à modifier" 
        nouveau_mot = simpledialog.askstring("Modifier le mot", "Saisissez le nouveau mot :", initialvalue=mot_a_modifier)
        if nouveau_mot:
            # Modifier le mot_a_modifier par nouveau_mot dans la base de données
            # Code pour modifier le mot dans la base de données
            simpledialog.showinfo("Succès", "Le mot a été modifié avec succès.")

    def supprimer_mot(self):
        mot_a_supprimer = "Mot à supprimer"  # Remplacez cette ligne par le code pour obtenir le mot à supprimer
        confirmation = simpledialog.askyesno("Confirmation", f"Êtes-vous sûr de vouloir supprimer le mot : {mot_a_supprimer} ?")
        if confirmation:
            # Supprimer le mot_a_supprimer de la base de données
            # Code pour supprimer le mot de la base de données
            simpledialog.showinfo("Succès", "Le mot a été supprimé avec succès.")
    
    
    

                                            
    

app = App()
root = Tk()

canevas = Canvas(root, width=333, height=361, background="ivory")
canevas.pack(side=LEFT)

root.geometry("666x361")
root.configure(background="#f7f8d9")
tracer = Button(root, text="A", command=app.tracer)
tracer.pack()
 

quitter = Button(root, text="Quitter", command=root.destroy)
quitter.pack(side=BOTTOM)
root = Tk()
# =======================================================================================================
# Partie menu :fichier, edition, aide.
# =======================================================================================================
 

 


# ======================================================================
# frame fenetre presentation
# ======================================================================
frame1 = Frame(master=root, width=333, height=361, bg="#f7f8d9")
frame1.grid(row=0, column=0)

frame2 = Frame(master=root, width=333, bg="")
frame2.grid(row=0, column=1)

# ======================================================================
# menu
# ======================================================================
import tkinter as tk
from bdd_et_theme import fmenu
# from pendu_et_clavier import*

# =======================================================================================================
# bdd et mot aleatoire
# =======================================================================================================

# menu onglet fichier
def fonction_a_executer():
    print(fmenu())

# menu onglet qui relance une nouvelle partie
def fonction_b_executer():
    
    global end, mot_en_progres, secret, cpt, annonce  # Déclarer annonce comme variable globale

    # Réinitialiser les variables du jeu
    secret = mot_en_progres
    mot_en_progres = list("_" * len(secret))
    stars = "".join(mot_en_progres)
    lbl["text"] = stars

    for btn in btns:
        btn["state"] = NORMAL

    cpt = 0
    end = False
    annonce["text"] = 0  # Remettre l'annonce à zéro

def fonction_c_executer():
    frame1 = Frame(master=root, width=333, height=361, bg="grey")
    frame1.grid(row=0, column=0)
    
# ========================================================================================





# fonction qui creer les onglets
def creer_menu():
    from tkinter import simpledialog
    menu = tk.Menu(root)    
    menu_fichier = tk.Menu(menu, tearoff=0)
    menu_fichier.add_command(label="Nouvelle partie", command=fonction_b_executer)
    menu_fichier.add_command(label="Choisir theme", command=fonction_a_executer)
    menu_fichier.add_command(label="Apparence", command=fonction_c_executer )
    menu_fichier.add_command(label="Quiter", command=quit)
    menu.add_cascade(label="Fichier", menu=menu_fichier)
    
    # ==========================================================================
    # Création du menu principal 'Edition'
    # ==========================================================================

    menuEditer  = Menu(menu, tearoff = 0) 
    menu.add_cascade(label="Edition",menu=menuEditer)
       
    # ==========================================================================
    #  Création des sous menus : 'Editer les mots', 'Editer les niveaux' 
    # ==========================================================================


    # Editer les mots
    menuMots = Menu(menuEditer, tearoff=0)
    menuEditer.add_cascade(label="Les mots", menu=menuMots)
    menuMots.add_command(label="Lire un mot", command=app.lire_mot)
    menuMots.add_command(label="Ajouter un mot", command=app.ecrire_mot)
    menuMots.add_command(label="Modifier un mot", command=app.modifier_mot)
    menuMots.add_command(label="Supprimer un mot", command=app.supprimer_mot)
    # Editer les niveaux
    menuThemes = Menu(menuEditer, tearoff=0)
    menuEditer.add_cascade(label="Les thèmes", menu=menuThemes)
    menuThemes.add_command(label="Lire un thème", )
    menuThemes.add_command(label="Ajouter un thème", )
    menuThemes.add_command(label="Modifier un thème", )
    menuThemes.add_command(label="Supprimer un thème", )
    
    from tkinter import messagebox
    def a_propos():
        messagebox.showinfo("À Propos", "Jeu du Pendu version 1.0\nCréé par [pb] ce logiciel est sous la licence libre GPL 3 ")


    # Création du menu principal 'Aide'
    menuAide  = Menu(menu, tearoff = 0) 
    menu.add_cascade(label="Aide", font='arial', menu=menuAide)

    # Création des sous menus : 'Editer les mots', 'Editer les niveaux'
    menuAide.add_command(label="A propos",command=a_propos )

     
    # menuAide.add_command(label="ce logiciel est sous la licence libre GPL 3 " )

    # configuration de la barre des menus
    root.config(menu= menu)

    root.config(menu=menu)

# execution des fonctions menu
creer_menu()
# =======================================================================================================
# bdd et mot aleatoire
# =======================================================================================================
 
# secret represente le mot a trouver,  code qui va mettre à jour le mot en recherche
def maj_mot_en_progres(mot_en_progres, lettre, secret):
    n = len(secret)
    for i in range(n):
        if secret[i] == lettre:
            mot_en_progres[i] = lettre
            
# si a la fin de la recherche le nombre de coup est depasse alors le pouce se met en bas
# Si la lettre cliquée par le joueur n’est pas dans le mot inconnu (ligne 3),
# le compteur d’erreurs augmente de 1 (ligne 4)
# et s’il dépasse la limite (ligne 5), c’est que la partie est perdue (ligne 6)
def score(lettre):
    global cpt, end
    if lettre not in secret:
        cpt += 1
        if cpt >= limite:
            
            annonce["text"] = "👎 "
            end = True
        else:
            annonce["text"] = cpt
    elif mot_en_progres == list(secret):
        annonce["text"] = '👍'
        end = True


# action sur bouton declenche execution de la fonction choisir_lettre
def choisir_lettre(event):
    if end:
        return
    # je capture l evenement au clic du bouton concerné
    mon_btn = event.widget
    # j obtiens le text correspondant au bouton 
    lettre = mon_btn["text"]

    mon_btn["state"] = DISABLED
     

    maj_mot_en_progres(mot_en_progres, lettre, secret)
    lbl["text"] = "".join(mot_en_progres)
    score(lettre)

def init():
    # def dessin():
    #     tracer = Button(root, text="A", command=app.tracer)
    #     tracer.pack()


    global end, mot_en_progres, secret, cpt
    # varaible du mot a trouver
    secret = "ESPERLOUETTE"
    mot_en_progres = list("_" * len(secret))
    # methode join transforme une liste de caractere en chaine de caractere
    stars = "".join(mot_en_progres)

    lbl["text"] = stars
    for btn in btns:
        btn["state"] = NORMAL
         
    # cpt = app.tracer
    cpt=0
    end = False

# limite d essai qui correspond a la construction du dessin de pendu qui marche pas
limite = 11

# affichage du nombre de coup
annonce = Label(frame1, width=8, font="Times 15 bold", text=0)
annonce.grid(padx=100, pady=50)
# annonce = Label(frame1, width=8, )
# annonce.grid(padx=100, pady=50)
 
# affichage de la ligne en pointillé pour ecrire le mot 
lbl = Label(frame2, font=('Deja Vu Sans Mono', 10, 'bold'), width=50, fg="black")
lbl.grid(row=0, column=1,padx=0, pady=0)

lettres = Frame(frame2)
lettres.grid(row=1, column=1,padx=40, pady=0)
# =======================================================================================================
# partie clavier
# =======================================================================================================
 
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
btns = []

# fabrication de deux ligne  de clavier de 10 caracteres, boucle qui a chaque iteration ecrit les 
# lettres de l alphabet contenu dans la variable ALPHA
for i in range(2):
    for j in range(10):
        btn = Button(lettres, text=ALPHA[10 * i + j], relief=FLAT, font='roboto 15',)
        btn.grid(row=i, column=j)
        btn.bind("<Button-1>", choisir_lettre)
        btns.append(btn)
# fabrication d une ligne de clavier de 6 caracteres, boucle qui a chaque iteration ecrit les 
# lettres de l alphabet contenu dans la variable ALPHA
for j in range(6):
    btn = Button(lettres, text=ALPHA[20 + j], relief=FLAT, font='roboto 15',activebackground='yellow')
    btn.grid(row=2, column=j + 2)
    btn.bind("<Button-1>", choisir_lettre)
    btns.append(btn)

init()





# =======================================================================================================
# bdd
# =======================================================================================================

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

    resultat_label = tk.Label(fenetre, text="", font=("Helvetica", 22))
    resultat_label.pack(pady=10)



    # Lancement de la boucle principale de la fenêtre
    fenetre.mainloop()

 





root.mainloop()
