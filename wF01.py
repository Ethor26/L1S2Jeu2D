# ======================================================
# PROJET TRANSVERSE 1 L1 : Jeu 2D Python
# Auteurs : Equipe ShirosakiBest = Ethan SUISSA, Lilandra ALBERT-LAVAULT, Pierre REY, Jean-Alexis TADDEI, Ludwig
# NEUBERTH- EFREI -L1 BN
# Date : 4 mai 2021 (?)
# Fichier F01 = "ECRAN D'ACCUEIL"

# ======================================================
from tkinter import *

from wF02 import F02
from wF03 import F03


class F01(Tk):

    # Constructeur de l'objet F01 : ne pas supprimer !!!
    def __init__(self):
        Tk.__init__(self)
        self.title("F01")  # Le titre de la fenêtre
        self.minsize(1200, 700)  # taille de fenêtre
        self.createWidgets() # Une méthode séparée pour construire le contenu de la fenêtre

    # Méthode/fonction de création des widgets
    def createWidgets(self):
        self.grid()  # Choix du mode d'arrangement

        # Création des widgets (boutons, labels, etc...)


        # ...........< L A B E L S > .........................
        # ELEMENT GRAPHIQUE : <Label> = [Libellé T04] : ...??
        # ??? A FAIRE

        # ELEMENT GRAPHIQUE : <Label> = [Libellé T05] : ...??
        # ??? A FAIRE

        # ELEMENT GRAPHIQUE : <Label> = [Libellé T06] : ...??
        # ??? A FAIRE

        # ELEMENT GRAPHIQUE : <Label> = [Libellé T07] : ...??
        # ??? A FAIRE

        # ELEMENT GRAPHIQUE : <Label> = [Libellé T08] : ...??
        # ??? A FAIRE


        # ...........< E N T R Y ' S > .......................
        # ELEMENT GRAPHIQUE : <Entry> = [Libellé E01] : Entrée du pseudo
        # ??? A FAIRE

        # ...........< B U T T O N S >........................
        # ELEMENT GRAPHIQUE : <Button> = [Bouton B02] : jouer
        self.ouvreF02 = Button(self, text="jouer", command=self.commandeOuvreF02)
        self.ouvreF02.place(x=10, y=600)

        self.ouvreF02 = Button(self, text="Configuration Commandes", command=self.commandeOuvreF03)
        self.ouvreF02.place(x=10, y=400)

        # ELEMENT GRAPHIQUE : <Button> = [Bouton B03] : ...??
        # ??? A FAIRE

        # ELEMENT GRAPHIQUE : <Button> = [Bouton B04] : ...??
        # ??? A FAIRE

        # ELEMENT GRAPHIQUE : <Button> = [Bouton B05] : ...??
        # ??? A FAIRE

        # ELEMENT GRAPHIQUE : <Button> = [Bouton B06] : ...??
        # ??? A FAIRE

        # ELEMENT GRAPHIQUE : <Button> = [A preciser] : Un bouton pour quitter l'application
        self.quitButton = Button(self, text="Quitter",command=self.destroy)
        self.quitButton.place(x=150, y=600)


        # ...........< L I S T B O X ' S > .......................
        # ELEMENT GRAPHIQUE : <ListBox> = [Listes L01] : Entrée du pseudo
        # ??? A FAIRE
        # (Tkinter)LISTBOX : Liste des ID des joueurs de la base de données (déclaration & position)
        AffID = Listbox(self)
        AffID.place(x=400, y=26, width=100, height=500)

        # (Tkinter)LISTBOX : Liste des noms des joueurs de la base de données (déclaration & position)
        AffNom = Listbox(self)
        AffNom.place(x=500, y=26, width=100, height=500)

        # (Tkinter)LISTBOX : Liste des score des joueurs de la base de données (déclaration & position)
        AffScore = Listbox(self)
        AffScore.place(x=600, y=26, width=100, height=500)

        # (Tkinter)LISTBOX : Liste des Angles des joueurs de la base de données (déclaration & position)
        AffAngle = Listbox(self)
        AffAngle.place(x=700, y=26, width=100, height=500)
    # ==================================================
    # D'autres méthodes :
    # ==================================================

    # ??? A comleter en fonction des besoins

    # COMMANDE : ouvre F02 (Jouer)
    def commandeOuvreF02(self):
        self.destroy()  # ferme F01
        # ouvre F02
        app = F02()         # implémente l'objet app
        app.focus_force()   # Force le focus sur la fenetre
        app.mainloop()

    def commandeOuvreF03(self):
        self.destroy()  # ferme F01
        # ouvre F02
        app = F03()         # implémente l'objet app
        app.mainloop()
