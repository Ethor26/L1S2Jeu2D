# ======================================================
# PROJET TRANSVERSE 1 L1 : Jeu 2D Python
# Auteurs : Equipe ShirosakiBest = Ethan SUISSA, Lilandra ALBERT-LAVAULT, Pierre REY, Jean-Alexis TADDEI, Ludwig
# NEUBERTH- EFREI -L1 BN
# Date : 4 mai 2021 (?)
# Fichier F02 = "JEUX EN ACTION"
# ======================================================
# from tkinter import *
import math
# from pygame import event
from tkinter import *
# from Tools import *
from math import *
import wF01


class F02(Tk):


    # Constructeur de l'objet F02 : ne pas supprimer !!!
    def __init__(self):
        Tk.__init__(self)
        self.title("F02")  # Le titre de la fenêtre
        self.minsize(1200, 700)  # taille de fenêtre

        # Une méthode séparée pour construire le contenu de la fenêtre
        self.Largeur = 1000  # Largeur de la zone de jeu
        self.Hauteur = 500  # Hauteur de la zone de jeu
        self.Rayon = 10  # rayon de l'objet Personnage

        # position initiale du perso
        self.PosX = 230
        self.PosY = 150

        # Creation des elements graphiques
        self.createWidgets()

    # Méthode de création des widgets
    def createWidgets(self):
        self.grid()  # Choix du mode d'arrangement

        # Version fonction
        def CommandeClavier(event2):
            """ Gestion de l'événement Appui sur une touche du clavier """
            touche = event2.keysym  # Un événement (event) est la survenue d’une action (clavier, souris) dont votre application a besoin d’être informée

            # Si touche ? => deplt a droite
            # A CODER

            # Si touche ? => deplt a Gauche
            # A CODER

            # Si touche ? => deplt a bas
            # A CODER

            # Si touche ? => deplt a Haut
            # A CODER

            if touche == 'p':
                self.PosY = self.ValeurPosY(self.PosY, 4)
                self.PosX = self.ValeurPosX(self.PosX, 4)

            print("posY = ", self.PosY)  # pour controle
            print("posX = ", self.PosX)  # pour controle
            print("Pion = ", PersoPion)  # pour controle

            CanevasJeu.coords(PersoPion, self.PosX - 10, self.PosY - 10, self.PosX + 10, self.PosY + 10)
            # on dessine le pion à sa nouvelle position

        # ...........< C A N V A S >........................
        # ELEMENT GRAPHIQUE : <Canvas> = G01 (fond noir ou se deroule le jeu)
        CanevasJeu = Canvas(self, width=self.Largeur, height=self.Hauteur, bg='black')
        CanevasJeu.pack(side=TOP, padx=5, pady=5)
        CanevasJeu.focus_set()  # crée un cadre autour du canvas et permet l'activation de bind
        CanevasJeu.bind('<Key>', CommandeClavier) # Met en relation les touches du clavier et les commandes.
        # Utiliser KeyPress-a pour appuyer sur a minuscule
        CanevasJeu.pack(padx=5, pady=5) # Pour placer le Canevas

        # ELEMENT GRAPHIQUE : <Personnage Pion> = G01 (Perso qui bouge par les commandes)
        PersoPion = CanevasJeu.create_oval(self.PosX - 10, self.PosY - 10, self.PosX + 10, self.PosY + 10, width=2, outline='black', fill='red')
        # A COMPLETER !!!

        # ...........< B U T T O N S >........................
        # ELEMENT GRAPHIQUE : <Button> = [Bouton B07] : Retour au menu (Retour F01)
        self.B07_retourMenu = Button(self, text="Retour Menu", command=self.commandeOuvreF01)
        self.B07_retourMenu.place(x=10, y=600)

        # ELEMENT GRAPHIQUE : <Button> = [A preciser] : Un bouton pour quitter l'application
        self.quitButton = Button(self, text="Quitter",command=self.destroy)
        self.quitButton.place(x=150, y=600)


        # =============================================================================

    # ==================================================
    # D'autres méthodes :
    # ==================================================

    # >>>>> A COMPLETER !!!
    # >>>>> A COMPLETER !!!
    # >>>>> A COMPLETER !!!

    def ValeurAngle(self):
        # codage à faire : Récupérer angle dans score.txt
        angle = math.radians(45)
        return angle

    # FONCTION OUTIL: Calcul de la commande programmable. Auteur : Ethan SUISSA - En cours
    def CalcProg(self, angle, VarX):
        v0 = 10 ** 2
        g = 9.81
        Eqmouv = (-1 / 2) * ((g * VarX ** 2) / (v0 * cos(angle)) ** 2) + tan(angle) * VarX
        return (Eqmouv)

    def ValeurPosX(self, valInit, VarX):
        valPosX = valInit + VarX
        # Verifie que l'on ne sort pas du cadre à droite ou à gauche
        if valPosX > self.Largeur - self.Rayon or valPosX - self.Rayon < 0:
            valPosX = valInit - self.Rayon
        return valPosX

    def ValeurPosY(self,valInit, VarX):
        ParametreAngle = self.ValeurAngle()
        valPosY = valInit - int(self.CalcProg(ParametreAngle, VarX))

        if valPosY < self.Rayon:
            valPosY = valInit + self.Rayon
        return valPosY



    # COMMANDE = ouvre F01,  (retour au menu)
    def commandeOuvreF01(self):
        # Ferme la fenetre
        self.destroy()  # ferme F02

        # Enregistre l'état du jeux et le score dans le fichier scores.txt:
        # >>>>>> ??A FAIRE

        # ouvre F01
        app = wF01.F01()
        app.mainloop()
