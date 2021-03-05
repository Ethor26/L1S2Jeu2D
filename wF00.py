# ======================================================
# PROJET TRANSVERSE 1 L1 : Jeu 2D Python
# Auteurs : Equipe ShirosakiBest = Ethan SUISSA, Lilandra ALBERT-LAVAULT, Pierre REY, Jean-Alexis TADDEI, Ludwig
# NEUBERTH- EFREI -L1 BN
# Date : 4 mai 2021 (?)
# Fichier F00
# ======================================================
from tkinter import *
from wF01 import F01


class F00(Tk):
    # Constructeur de l'objet F01 : ne pas supprimer !!!
    def __init__(self, message):
        Tk.__init__(self)
        self.title("F00")  # Le titre de la fenêtre

        self.minsize(1200, 700)  # taille de fenêtre

        # Une méthode séparée pour construire le contenu de la fenêtre
        self.createWidgets()

        print(message)  # A supprimer : controle/test de passage de valeur à la classe par son constructeur

    # Méthode de création des widgets
    def createWidgets(self):
        self.grid()  # Choix du mode d'arrangement

        # Création des widgets :

        # ...........< L A B E L S > .........................
        # ELEMENT GRAPHIQUE : <Label> = [Libellé T01] : ...??
        # ??? A FAIRE

        # ELEMENT GRAPHIQUE : <Label> = [Libellé T02] : ...??
        # ??? A FAIRE

        # ELEMENT GRAPHIQUE : <Label> = [Libellé T03] : ...??
        # ??? A FAIRE
        # ...........

        # ...........< B U T T O N S >........................
        # ELEMENT GRAPHIQUE : <Button> = [Bouton B01] : ouvrir menu (F01)
        self.ouvreF01 = Button(self, text="Start", command=self.commandeOuvreF01)
        self.ouvreF01.place(x=10, y=600)

        # ELEMENT GRAPHIQUE : <Button> = [A preciser] : Un bouton pour quitter l'application
        self.quitButton = Button(self, text="Quitter", command=self.destroy)
        self.quitButton.place(x=150, y=600)

    # ==================================================
    # D'autres méthodes :
    # ==================================================

    # COMMANDE = ouvre F01,  et ferme F00 (retour au menu)
    def commandeOuvreF01(self):
        self.destroy()  # ferme F00
        # ouvre F01
        app = F01()  #
        app.mainloop()
