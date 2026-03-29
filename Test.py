import tkinter as tk
import random

fenetre = tk.Tk()
fenetre.title("Jeu du Pendu - Margaux Le Coq Fridoflssson")
fenetre.geometry("800x600")
fenetre.configure(bg="#F5F5F5")

canevas = tk.Canvas(fenetre, width=400, height=300, bg="#9BC7EB")
canevas.pack(pady=10)

liste_mots = ["POMME","BANANE","ORANGE","FRAISE","MANGUE", "CAROTTE","TOMATE","POIVRON",
                           "BROCOLI","OIGNON","FRANCE","CANADA", "JAPON","BRESIL","MAROC",
                           "PARIS","LONDRES","TOKYO","ROME","BERLIN","PLAGE","FORET","DESERT","MONTAGNE", "OCEAN"
                           ]

mot_secret = random.choice(liste_mots)

lettres_trouvees = []
erreurs = 0
max_erreurs = 6

label_mot = tk.Label(fenetre, text="", font=("Courier", 24), bg="#B690A2")
label_mot.pack(pady=5)
label_message = tk.Label(fenetre, text="", font=("Arial", 16, "bold"), bg="#F5F5F5")
label_message.pack(pady=5)


def afficher_mot():
    affichage = ""
    
    for lettre in mot_secret:
        if lettre in lettres_trouvees:
            affichage += lettre + " "
        else:
            affichage += "_ "
    
    label_mot.config(text=affichage)
afficher_mot()

fenetre.mainloop()
