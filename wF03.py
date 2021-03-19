# ======================================================
# PROJET TRANSVERSE 1 L1 : Jeu 2D Python
# Auteurs : Equipe ShirosakiBest = Ethan SUISSA, Lilandra ALBERT-LAVAULT, Pierre REY, Jean-Alexis TADDEI, Ludwig
# NEUBERTH- EFREI -L1 BN
# Date : 4 mai 2021 (?)
# Fichier F03 = "CONFIGURATION DES COMMANDES"
# ======================================================
from tkinter import *
import math
import wF01


class F03(Tk):
    # Constructeur de l'objet F03 : ne pas supprimer !!!
    def __init__(self): # NomJoueur a ajouter en paramètre ?
        Tk.__init__(self)
        self.title("F03")  # Le titre de la fenêtre
        self.minsize(1200, 700)  # taille de fenêtre
        # Une méthode séparée pour construire le contenu de la fenêtre
        self.createWidgets()

    # Méthode de création des widgets
    def createWidgets(self):
        self.grid()  # Choix du mode d'arrangement des elements

        def RecupAngle(): # Récupération angle de la zone de Saisie ou pose de 0
            TextAngleEnDegree = entreAngle.get()
            # Fonction doit être mise avant sinon erreur
            AngleEnDegree = 0
            msg = "..."
            if TextAngleEnDegree != "":
                try:
                    AngleEnDegree = int(TextAngleEnDegree)
                except ValueError:
                    msg = ">> Angle doit etre un entier "  # Message d'information pour l'utilisateur
                    print(msg)  # Pour contrôle en console
            self.messageUtilisateurAngle.set(msg)
            print(str(self.messageUtilisateurAngle.get()))  # Pour Controle
            print("Angle en degree = ", AngleEnDegree)   # Pour controle
            # Etape 2 : Envoi de l'angle dans score.txt
            # A FAIRE QUAND BASE PRETE


        # Création des widgets (boutons, labels, etc...)
        # ...........< T E X T E S > .......................
        # ELEMENT GRAPHIQUE : <Texte> = [à definir] annoncant la saisie de l'angle # A REPOSITIONNER !!!
        lblEntreAngle = Label(self, text="Angle=")  # Nom de la fenêtre en rouge à déclarer comme au dessus (avec le nom
        # de fenêtre qu'on veut
        lblEntreAngle.place(x=150, y=200)

        # ...........< E N T R Y ' S > .......................
        # ELEMENT GRAPHIQUE : <Entry> = [à definir] pour saisir l'angle # A REPOSITIONNER !!!

        entreAngle = Entry(self)
        entreAngle.place(x=200, y=200, width=50)  # A placer à coté du bouton "Appliquer", écart de 50 entre les x
        # Variable(s)
        self.messageUtilisateurAngle = StringVar()  # Variable de message d'erreur de saisie type stringvar() pour maj Label
        self.messageUtilisateurAngle.set("...")
        # pertinent.

        # ...........< B U T T O N S >........................

        # ELEMENT GRAPHIQUE : <Button> = [Bouton B09] : "Appliquer (Enregistrer) l'angle"
        # >>>>> ??? a faire
        self.AppliqAngle = Button(self, text="Appliquer l'angle", command=RecupAngle)
        self.AppliqAngle.place(x=250, y=200)

        # ELEMENT GRAPHIQUE : <Button> = [Bouton B07 bis] : Retour au menu (Retour F01)
        self.B07_retourMenu = Button(self, text="Retour Menu", command=self.commandeOuvreF01)
        self.B07_retourMenu.place(x=10, y=600)

        # ELEMENT GRAPHIQUE : <Button> = [A preciser] : Un bouton pour quitter l'application
        self.quitButton = Button(self, text="Quitter",command=self.destroy)
        self.quitButton.place(x=150, y=600)

        # ==================================================

    # D'autres méthodes :
    # ==================================================

    # COMMANDE = Enregistre l'angle dans le fichier score
    # >>>>> ??? 1 Faire !!!!

    # COMMANDE = ouvre F01,  (retour au menu)
    def commandeOuvreF01(self):
        # Ferme la fenetre
        self.destroy()  # ferme F03
        # ouvre F01
        app = wF01.F01()
        app.mainloop()
