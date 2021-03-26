# ======================================================
# PROJET TRANSVERSE 1 L1 : Jeu 2D Python
# Auteurs : Equipe ShirosakiBest = Ethan SUISSA, Lilandra ALBERT-LAVAULT, Pierre REY, Jean-Alexis TADDEI, Ludwig
# NEUBERTH- EFREI -L1 BN
# Date : 4 mai 2021 (?)
# Fichier F04 = "RESULTATS DU JEUX"
# ======================================================
from tkinter import *

import wF01


class F04(Tk):
    # Constructeur de l'objet F04 : ne pas supprimer !!!
    def __init__(self):
        Tk.__init__(self)
        self.title("F04")  # Le titre de la fenêtre
        self.minsize(1200, 700)  # taille de fenêtre
        # Une méthode séparée pour construire le contenu de la fenêtre
        self.createWidgets()

    # Méthode de création des widgets
    def createWidgets(self):
        self.grid()  # Choix du mode d'arrangement des elements

    # ==================================================
    # FONCTIONS WIDGETS::::::::

    # ==================================================
    # ELEMENTS GRAPHIQUES::::::::

        # Création des widgets (boutons, labels, etc...)
        # ...........
        # ...........

        # ...........< L A B E L S > .........................
        # ELEMENT GRAPHIQUE : <Label> = [A definir] : Afficher Score, nom, ...
        # >>>>> ??? plusieurs elements a faire !!!



        # ...........< B U T T O N S >........................
        # ELEMENT GRAPHIQUE : Bouton B07 bis : Retour au menu (Retour F01)
        self.B07_retourMenu = Button(self, text="Retour Menu", command=self.commandeOuvreF01)
        self.B07_retourMenu.place(x=10, y=600)

        # ELEMENT GRAPHIQUE : Un bouton pour quitter l'application
        self.quitButton = Button(self, text="Quitter",command=self.destroy)
        self.quitButton.place(x=150, y=600)

    # ==================================================
    # AUTRES FONCTIONS::::::::

    # COMMANDE = Rejouer
    # >>>>> ??? 1 Faire !!!!

    # COMMANDE = ouvre F01,  (retour au menu)
    def commandeOuvreF01(self):
        # Ferme la fenetre
        self.destroy()  # ferme F04

        # ouvre F01
        app = wF01.F01()
        app.mainloop()
