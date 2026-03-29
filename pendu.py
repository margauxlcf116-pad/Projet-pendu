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

def verifier_lettre():
    global erreurs

    lettre = entree.get().upper()
    entree.delete(0, tk.END)

    if len(lettre) != 1:
        return

    if lettre in mot_secret:
        if lettre not in lettres_trouvees:
            lettres_trouvees.append(lettre)
    else:
        erreurs += 1
        dessiner_chien(erreurs)

    afficher_mot()

    # Vérifier victoire
    if all(lettre in lettres_trouvees for lettre in mot_secret):
        label_message.config(text="Bravo ! Tu as gagné !", fg="green")

    # Vérifier défaite
    if erreurs == max_erreurs:
        label_message.config(text="Perdu ! Le mot était : " + mot_secret, fg="red")


def dessiner_chien(nb_erreurs):

    if nb_erreurs == 1:
        # Corps
        canevas.create_oval(200, 170, 340, 240, fill="#C19A6B", outline="black", width=2)

    elif nb_erreurs == 2:
        # Tête
        canevas.create_oval(130, 140, 210, 220, fill="#C19A6B", outline="black", width=2)

    elif nb_erreurs == 3:
        # Oreilles
        canevas.create_oval(115, 150, 145, 210, fill="#8B5A2B", outline="black")
        canevas.create_oval(195, 150, 225, 210, fill="#8B5A2B", outline="black")

    elif nb_erreurs == 4:
        # Yeux
        canevas.create_oval(150, 170, 160, 180, fill="white", outline="black")
        canevas.create_oval(175, 170, 185, 180, fill="white", outline="black")

        canevas.create_oval(153, 173, 157, 177, fill="black")
        canevas.create_oval(178, 173, 182, 177, fill="black")

    elif nb_erreurs == 5:
        # Museau
        canevas.create_oval(155, 185, 185, 205, fill="#EED5B7", outline="black")

        # Nez
        canevas.create_oval(165, 190, 175, 198, fill="black")

    elif nb_erreurs == 6:
        # Pattes
        canevas.create_rectangle(230, 230, 250, 260, fill="#C19A6B", outline="black")
        canevas.create_rectangle(300, 230, 320, 260, fill="#C19A6B", outline="black")

        # Queue
        canevas.create_line(340, 190, 370, 160, width=6)

        # Os
        canevas.create_oval(190, 195, 205, 210, fill="white", outline="black")
        canevas.create_rectangle(200, 200, 230, 205, fill="white", outline="black")
        canevas.create_oval(225, 195, 240, 210, fill="white", outline="black")

entree = tk.Entry(fenetre, font=("Gabriola", 16), justify="center")
entree.pack(pady=5)

bouton_valider = tk.Button(
    fenetre,
    text="Valider",
    font=("Gabriola", 16, "bold"),
    bg="#E75888",
    fg="white",
    activebackground="#D48FAB",
    activeforeground="white",
    width=16,
    height=1,
    relief="flat",
    bd=0,
    command=verifier_lettre)

bouton_valider.pack(pady=5)

fenetre.mainloop()
