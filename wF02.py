# ======================================================
# PROJET TRANSVERSE 1 L1 : Jeu 2D Python
# Auteurs : Equipe ShirosakiBest = Ethan SUISSA, Lilandra ALBERT-LAVAULT, Pierre REY, Jean-Alexis TADDEI, Ludwig
# NEUBERTH- EFREI -L1 BN
# Date : 4 mai 2021 (?)
# Fichier F02 = "JEUX EN ACTION"
# ======================================================
import math
# import os
from tkinter import *
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
        # Temps initial
        self.Temps = 0
        # 1ere position finale (confondue avec initiale)
        self.valY_Final = 0
        self.valX_Final = 0
        # Pas de rebond de départ
        # self.rebond = False
        # Creation des elements graphiques
        self.createWidgets()

    # Méthode de création des widgets
    def createWidgets(self):
        self.grid()  # Choix du mode d'arrangement

        # Fonction qui définit l'action lorsque l'on actionne une touche
        def CommandeClavier(event):
            touche = event.keysym  # Un événement (event) est la survenue d’une action (clavier, souris) dont votre application a besoin d’être informée

            # Si touche ? => deplt a droite
            # A CODER !!!

            # Si touche ? => deplt a Gauche
            # A CODER !!!

            # Si touche ? => deplt a bas
            # A CODER !!!

            # Si touche ? => deplt a Haut
            # A CODER !!!

            # Si touche p => déplacement selon equation de mouvement
            if touche == 'p':
                print("Info:  touche p activée ***")
                deplacement_P()

        # =============================================================================
        # Fonction de déplacement de la touche P. Auteur : Ethan SUISSA - Terminé
        def deplacement_P():
            nbRebond = 0
            self.Temps += 0.0001

            self.PosX, self.PosY, self.siRebond, Temps = self.ValeurPosXY(self.PosX, self.PosY, self.Temps)

            print("posY = ", self.PosY)  # pour controle
            print("posX = ", self.PosX)  # pour controle
            print("Pion = ", PersoPion)  # pour controle
            print("Temps = ", Temps)  # pour controle

            # Positionnne le personnage
            CanevasJeu.coords(PersoPion, self.PosX - 10, self.PosY - 10, self.PosX + 10, self.PosY + 10)

            # S'il y a un rebond sur le côté
            if self.siRebond:
                nbRebond = nbRebond + 1
                print("Nombre de rebond = ", nbRebond)

            # On déclenche le déplacement toute les 3 ms
            idAfter = self.after(1, deplacement_P)

            # On arrête le déplacement s'il y a un rebond ou si le facteur temps est supérieur à 0.05
            if nbRebond > 0 or self.Temps > 0.05:  # 0.07 pour courbe complète
                self.after_cancel(idAfter)
                self.Temps = 0
                nbRebond = 0

        # ...........< C A N V A S >........................
        # ELEMENT GRAPHIQUE : <Canvas> = G01 (fond noir ou se deroule le jeu)

        CanevasJeu = Canvas(self, width=self.Largeur, height=self.Hauteur, bg='black')
        CanevasJeu.pack(side=TOP, padx=5, pady=5)
        CanevasJeu.focus_set()  # crée un cadre autour du canvas et permet l'activation de bind
        CanevasJeu.bind('<Key>', CommandeClavier)  # Met en relation les touches du clavier et les commandes.
        CanevasJeu.pack(padx=5, pady=5)  # Pour placer le Canevas

        # ELEMENT GRAPHIQUE : <Personnage Pion> = G01 (Perso qui bouge par les commandes)
        PersoPion = CanevasJeu.create_oval(self.PosX - 10, self.PosY - 10, self.PosX + 10, self.PosY + 10, width=2,
                                           outline='black', fill='red')

        # ...........< B U T T O N S >........................
        # ELEMENT GRAPHIQUE : <Button> = [Bouton B07] : Retour au menu (Retour F01)
        self.B07_retourMenu = Button(self, text="Retour Menu", command=self.commandeOuvreF01)
        self.B07_retourMenu.place(x=10, y=600)

        # ELEMENT GRAPHIQUE : <Button> = [A preciser] : Un bouton pour quitter l'application
        self.quitButton = Button(self, text="Quitter", command=self.destroy)
        self.quitButton.place(x=150, y=600)

        # =============================================================================

    def ValeurAngleParametreEnRadian(self):
        # Etape 1 : Récupération angle du fichier Score.txt.
        # A FAIRE QUAND BASE PRETE

        # Etape 2 : Conversion et envoi pour calcul commande programmable
        AngleEnDegree = 45   # Temporaire pour utiliser la commande programmable
        # Angles à tester : 26, 45, 60, 120, 210, 300, extremes (89, 179, 269, 359)
        print("Angle en degree = ", AngleEnDegree)  # Pour controle
        angleRadian = math.radians(AngleEnDegree)  # Conversion en radians pour calculs
        return angleRadian

    # FONCTION OUTIL : Utilise l'équation de mouvement pour calculer la postion finale en fonction de l'angle
    # Auteur : Ethan SUISSA - En cours
    def CalcProg(self, AngleDeduitDegree, Temps):
        v0 = 0.7  # Choix de vitesse à 5
        g = 9.81  # Constante de gravitation
        Angle_Deduit_Radian = math.radians(AngleDeduitDegree)  # convertion en Radian de l'angle deduit
        dx = v0 * cos(Angle_Deduit_Radian)
        if Angle_Deduit_Radian == 0.0:
            g = 0
        dy = -g * Temps + v0 * sin(Angle_Deduit_Radian)
        print("Angle radian:", Angle_Deduit_Radian)  # Test
        print("dx = :", dx, "dy = :", dy)  # Test
        return dx, dy

    # FONCTION OUTIL : Renvoie les valeurs de X et Y selon l'équation de mouvement et selon l'angle paramétré
    # Auteur : Ethan SUISSA - En cours
    def ValeurPosXY(self, valX_Initial, valY_Initial, Temps):
        print("ValPosXY :  valXInitial =", valX_Initial)
        print("ValPosXY :  valYInitial =", valY_Initial)
        rebond = False
        AngleEnDegree = degrees(self.ValeurAngleParametreEnRadian())
        # Bloc 1
        if 0 <= AngleEnDegree <= 90:
            print("ValPosXY :  Bloc 1 ")  # pour controle
            Dx, Dy = self.CalcProg(AngleEnDegree, Temps)
            self.valX_Final = valX_Initial + Dx
            self.valY_Final = valY_Initial - Dy

        # Bloc 2
        if 90 < AngleEnDegree <= 180:
            print("ValPosX :  Bloc 2 ")  # pour controle
            Angle_Deduit_Degree = AngleEnDegree - 90
            Dx, Dy = self.CalcProg(Angle_Deduit_Degree, Temps)
            self.valX_Final = valX_Initial - Dy
            self.valY_Final = valY_Initial - Dx

        # Bloc 3
        if 180 < AngleEnDegree <= 270:
            print("ValPosX :  Bloc 3 ")  # pour controle
            Angle_Deduit_Degree = AngleEnDegree - 180
            Dx, Dy = self.CalcProg(Angle_Deduit_Degree, Temps)
            self.valX_Final = valX_Initial - Dx
            self.valY_Final = valY_Initial + Dy

        # Bloc 4
        if 270 < AngleEnDegree <= 360:
            print("ValPosX :  Bloc 4  ")  # pour controle
            Angle_Deduit_Degree = AngleEnDegree - 270
            Dx, Dy = self.CalcProg(Angle_Deduit_Degree, Temps)
            self.valX_Final = valX_Initial + Dy
            self.valY_Final = valY_Initial + Dx

        print("ValPosXY : ValXFinal avant correction = ", self.valX_Final)
        print("ValPosXY : ValYFinal avant correction = ", self.valY_Final)

        # Corrige la position X si on sort du cadre
        # Rebond à droite
        if self.valX_Final > self.Largeur - self.Rayon:
            print("ValPosXY (posX):  Sortie du cadre à droite => Rebond ")
            self.valX_Final = valX_Initial - self.Rayon
            rebond = True

        # Rebond à gauche
        if self.valX_Final < self.Rayon:
            print("ValPosXY (posX):  Sortie du cadre à gauche => Rebond ")
            self.valX_Final = valX_Initial + self.Rayon
            rebond = True

        # Rebond en bas
        if self.valY_Final < self.Rayon:
            print("ValPosXY (posY):  Sortie en bas ==> Rebond")
            self.valY_Final = valY_Initial + self.Rayon
            rebond = True

        # Rebond en haut
        if self.valY_Final > self.Hauteur - self.Rayon:
            print("ValPosXY (posY):  Sortie en haut ==> Rebond")
            self.valY_Final = valY_Initial - self.Rayon
            rebond = True

        return self.valX_Final, self.valY_Final, rebond, Temps

    # COMMANDE = ouvre F01,  (retour au menu)
    # Auteur : Ethan SUISSA - En cours
    def commandeOuvreF01(self):
        # Ferme la fenetre
        self.destroy()  # ferme F02

        # Enregistre l'état du jeux et le score dans le fichier scores.txt:
        # >>>>>> ??A FAIRE

        # ouvre F01
        app = wF01.F01()
        app.mainloop()
