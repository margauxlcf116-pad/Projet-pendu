import tkinter as tk
import random

fenetre = tk.Tk()
fenetre.title("Jeu du Pendu - Margaux Le Coq Fridoflssson")
fenetre.geometry("800x600")
fenetre.configure(bg="#F5F5F5")

canevas = tk.Canvas(fenetre, width=500, height=400, bg="#9BC7EB")
canevas.pack(pady=20)

liste_mots = ["POMME","BANANE","ORANGE","FRAISE","MANGUE", "CAROTTE","TOMATE","POIVRON",
                           "BROCOLI","OIGNON","FRANCE","CANADA", "JAPON","BRESIL","MAROC",
                           "PARIS","LONDRES","TOKYO","ROME","BERLIN","PLAGE","FORET","DESERT","MONTAGNE", "OCEAN"
                           ]

mot_secret = random.choice(liste_mots)

lettres_trouvees = []
erreurs = 0
max_erreurs = 6

label_mot = tk.Label(fenetre, text="", font=("Courier", 24), bg="#B690A2")
label_mot.pack(pady=10)

def afficher_mot():
    affichage = ""
    
    for lettre in mot_secret:
        if lettre in lettres_trouvees:
            affichage += lettre + " "
        else:
            affichage += "_ "
    
    label_mot.config(text=affichage)
afficher_mot()

entree = tk.Entry(fenetre, font=("Kermit Extrabold Expanded", 14), justify="center")
entree.pack(pady=10)

bouton_valider = tk.Button(
    fenetre,
    text="Valider",
    font=("Gabriola", 14, "bold"),
    bg="#E75888",
    fg="white",
    activebackground="#D48FAB",
    activeforeground="white",
    width=12,
    height=1,
    relief="flat",
    bd=0,
    command=afficher_mot)

bouton_valider.pack(pady=15)

fenetre.mainloop()