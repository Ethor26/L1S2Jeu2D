# ======================================================
# PROJET TRANSVERSE 1 L1 : Jeu 2D Python
# Auteurs : Equipe ShirosakiBest = Ethan SUISSA, Lilandra ALBERT-LAVAULT, Pierre REY, Jean-Alexis TADDEI, Ludwig
# NEUBERTH- EFREI -L1 BN
# Date : 4 mai 2021 (?)
# Fichier F04 = "RESULTATS DU JEUX"
# ======================================================
#from tkinter import *
from wF01 import *
from Tools import *


class F04(Tk):
    # Constructeur de l'objet F04 : ne pas supprimer !!!
    def __init__(self, Score): # Importation du paramètre score de F02
        Tk.__init__(self)
        self.title("F04")  # Le titre de la fenêtre
        self.minsize(1200, 700)  # taille de fenêtre

        self.ScoreRec = Score
        # Une méthode séparée pour construire le contenu de la fenêtre
        self.createWidgets()


    # Méthode de création des widgets
    def createWidgets(self):
        self.grid()  # Choix du mode d'arrangement des elements

    # ==================================================
    # FONCTIONS WIDGETS::::::::
        self.VictoireJeu()

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
        self.quitButton = Button(self, text="Quitter", command=self.destroy)
        self.quitButton.place(x=150, y=600)

    # ==================================================
    # AUTRES FONCTIONS::::::::

    # COMMANDE = Rejouer
    # >>>>> ??? 1 Faire !!!!
    # ===============================
    # FONCTIONS statuant si le meilleur score est dépassé (en cours).
    def VictoireJeu(self):
        tab, nbLignes = open_score_file2()
        if self.ScoreRec >= int(tab[nbLignes - 1][3]):
            print("Meilleur score dépassé")
        else:
            print("Meilleur score non atteint")

    # COMMANDE = ouvre F01,  (retour au menu)
    def commandeOuvreF01(self):
        # Ferme la fenetre
        self.destroy()  # ferme F04

        # ouvre F01
        app = F01()
        app.mainloop()
