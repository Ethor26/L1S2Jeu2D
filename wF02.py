# ======================================================
# PROJET TRANSVERSE 1 L1 : Jeu 2D Python
# Auteurs : Equipe ShirosakiBest = Ethan SUISSA, Lilandra ALBERT-LAVAULT, Pierre REY, Jean-Alexis TADDEI, Ludwig
# NEUBERTH- EFREI -L1 BN
# Date : 4 mai 2021 (?)
# Fichier F02 = "JEUX EN ACTION"
# ======================================================
from tkinter import *

import wF01


class F02(Tk):
    # Constructeur de l'objet F02 : ne pas supprimer !!!
    def __init__(self):
        Tk.__init__(self)
        self.title("F02")  # Le titre de la fenêtre
        self.minsize(1200, 700)  # taille de fenêtre
        # Une méthode séparée pour construire le contenu de la fenêtre
        self.createWidgets()

    # Méthode de création des widgets
    def createWidgets(self):
        self.grid()  # Choix du mode d'arrangement

        # Création des widgets (boutons, labels, etc...)

        # ...........< C A N V A S >........................
        # ELEMENT GRAPHIQUE : <Canvas> = G01 (fond noir ou se deroule le jeu)
        Canvas(self, width=1000, height=500, bg='black').pack(side=TOP, padx=5, pady=5)
        # A COMPLETER !!!
        # A COMPLETER !!!

        # ...........< B U T T O N S >........................
        # ELEMENT GRAPHIQUE : <Button> = [Bouton B07] : Retour au menu (Retour F01)
        self.B07_retourMenu = Button(self, text="Retour Menu", command=self.commandeOuvreF01)
        self.B07_retourMenu.place(x=10, y=600)

        # ELEMENT GRAPHIQUE : <Button> = [A preciser] : Un bouton pour quitter l'application
        self.quitButton = Button(self, text="Quitter",command=self.destroy)
        self.quitButton.place(x=150, y=600)

    # ==================================================
    # D'autres méthodes :
    # ==================================================

    # >>>>> A COMPLETER !!!
    # >>>>> A COMPLETER !!!
    # >>>>> A COMPLETER !!!

    # COMMANDE = ouvre F01,  (retour au menu)
    def commandeOuvreF01(self):
        # Ferme la fenetre
        self.destroy()  # ferme F02

        # Enregistre l'état du jeux et le score dans le fichier scores.txt:
        # >>>>>> ??A FAIRE

        # ouvre F01
        app = wF01.F01()
        app.mainloop()
