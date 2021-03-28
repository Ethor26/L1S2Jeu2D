# ======================================================
# PROJET TRANSVERSE 1 L1 : Jeu 2D Python
# Auteurs : Equipe ShirosakiBest = Ethan SUISSA, Lilandra ALBERT-LAVAULT, Pierre REY, Jean-Alexis TADDEI, Ludwig
# NEUBERTH- EFREI -L1 BN
# Date : 4 mai 2021 (?)
# Fichier F02 = "JEUX EN ACTION"
# ======================================================
import math
# import os
import os
from tkinter import *
from math import *
from PIL import Image
from PIL.ImageTk import PhotoImage
import wF01
import wF04


class F02(Tk):

    # Constructeur de l'objet F02 : ne pas supprimer !!!
    def __init__(self):
        Tk.__init__(self)
        self.title("F02")  # Le titre de la fenêtre
        self.minsize(1200, 700)  # taille de fenêtre

        # Une méthode séparée pour construire le contenu de la fenêtre
        self.Largeur = 1200  # Largeur de la zone de jeu
        self.Hauteur = 680  # Hauteur de la zone de jeu
        self.Rayon = 10  # rayon de l'objet Personnage

        # position initiale du perso, respectivement X et Y
        self.PosX = 600
        self.PosY = 400
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

    # ==================================================
    # FONCTIONS WIDGET ::::::::

        # =============================================================================
        # FONCTION qui crée un déplacment lorsque l'on actionne une touche
        def CommandeClavier(event):
            self.touche = event.keysym  # Un événement (event) est la survenue d’une action (clavier, souris) dont votre
            # application a besoin d’être informée

            dir = 10

            # Si touche ? => deplt a droite
            # A CODER !!!
            if self.touche == 'd':
                print("Info:  touche d activée ***")
                self.PosX = self.ValeurPosX(self.PosX, dir)
            # Si touche ? => deplt a Gauche
            # A CODER !!!
            if self.touche == 'q':
                print("Info:  touche q activée ***")
                self.PosX = self.ValeurPosX(self.PosX, -dir)
            # Si touche ? => deplt a bas
            # A CODER !!!
            if self.touche == 's':
                print("Info:  touche s activée ***")
                self.PosY = self.ValeurPosY(self.PosY, -dir)
            # Si touche ? => deplt a Haut
            # A CODER !!!
            if self.touche == 'z':
                print("Info:  touche z activée ***")
                self.PosY = self.ValeurPosY(self.PosY, dir)
            # Si touche p => déplacement selon equation de mouvement

            if self.touche == 'p':
                print("Info:  touche p activée ***")
                deplacement_P()

        # =============================================================================
        # FONCTION de déplacement de la touche P. Auteur : Ethan SUISSA - Terminé
        def deplacement_P():
            nbRebond = 0 # Initialisation du nombre de rebond sur les côtés à chaque mouvement
            self.Temps += 0.00015 # Augmentation d'une variable de temps pour calcul Position Y (de commande
            # programmable) et permet de définir la limite du mouvement.
            # Récupération des nouvelles position
            self.PosX, self.PosY, self.siRebond, Temps = self.ValeurPosXY(self.PosX, self.PosY, self.Temps)

            print("posY = ", self.PosY)  # pour controle
            print("posX = ", self.PosX)  # pour controle
            print("Pion = ", self.PersoImgVaisseau)  # pour controle
            print("Temps = ", Temps)  # pour controle

            # Repositionnne le personnage
            self.CanevasJeu.coords(self.ImgPerso, self.PosX, self.PosY)

            # S'il y a un rebond sur un côté, augmente la variable du nombre de rebond
            if self.siRebond:
                nbRebond = nbRebond + 1
                print("Nombre de rebond = ", nbRebond)

            # On déclenche le déplacement toute les 1 ms, réactualisation de la fenêtre
            idAfter = self.after(1, deplacement_P)

            # On arrête le déplacement s'il y a un rebond ou si le facteur temps est supérieur à 0.05
            if nbRebond > 0 or self.Temps > 0.06:  # 0.07 pour courbe complète
                self.after_cancel(idAfter)
                self.Temps = 0
                nbRebond = 0

        # ==================================================
        # ELEMENTS GRAPHIQUES::::::::
        # ...........< I M A G E S >........................

        # ELEMENT GRAPHIQUE : <Canvas> = G01 (fond imagé ou se deroule le jeu)
        # Etape 1 : Création d'un Canevas noir
        self.CanevasJeu = Canvas(self, width=self.Largeur, height=self.Hauteur, bg='black')
        self.CanevasJeu.pack(side=TOP, padx=5, pady=5)

        # Etape2 : Ajout d'un Fond d'ecran sur le Canevas
        self.imageFond = Image.open(os.getcwd() + "/IMAGES/ImagesF02/fondSpatial-1.jpeg")
        # Slash doivent être ajoutés à coté de D: et juste avant le nom de l'image pour le chemin absolue, sinon on peut
        # importer une partie du chemin (celle où est wF02) avec la fonction os.getcwd().
        self.imgfondEcran = PhotoImage(self.imageFond)  # importe la photo du fond dans le fichier
        self.objImgFondEcran = self.CanevasJeu.create_image(self.Largeur // 2, self.Hauteur // 2,
                                                            image=self.imgfondEcran) # Implémentation de l'image dans le
        # Canevas du jeu

        self.CanevasJeu.focus_set()  # crée un cadre autour du canvas et permet l'activation de bind
        self.CanevasJeu.bind('<Key>', CommandeClavier)  # Met en relation les touches du clavier et les commandes.
        self.CanevasJeu.pack(padx=5, pady=5)  # Pour placer le Canevas
        self.CanevasJeu.tag_lower(self.objImgFondEcran)  # arriere plan, tag_raise pour premier plan

        # ELEMENT GRAPHIQUE : <PointesVaisseaux> = G01 : Eléments graphiques du fond

        # Vaisseau pointe Bas
        self.imageV1 = Image.open(os.getcwd() + "/IMAGES/ImagesF02/image-DestoyerImperial-3 Bas.png")
        self.imageV1 = self.imageV1.resize((150, 180), Image.ANTIALIAS)  # resize permet de mettre les photos au bon
        # format pour les inclure dans le canevas. Antialias = inconnu, permet à resize de fonctionner
        self.imgV1 = PhotoImage(self.imageV1) # Même principe que fond d'écran
        self.objImgV1 = self.CanevasJeu.create_image(self.Largeur // 2, self.Hauteur, image=self.imgV1)

        # Vaisseau pointe Haut : Même principe que pointe bas, valable pour toutes les pointes de vaisseaux
        self.imageV2 = Image.open(os.getcwd() + "/IMAGES/ImagesF02/image-DestoyerImperial-3 Haut.png")
        self.imageV2 = self.imageV2.resize((150, 180), Image.ANTIALIAS)
        self.imgV2 = PhotoImage(self.imageV2)
        self.objImgV2 = self.CanevasJeu.create_image(self.Largeur // 2, 0, image=self.imgV2)

        # Vaisseau pointe Droite
        self.imageV3 = Image.open(os.getcwd() + "/IMAGES/ImagesF02/image-DestoyerImperial-3 Droite.png")
        self.imageV3 = self.imageV3.resize((150, 180), Image.ANTIALIAS)
        self.imgV3 = PhotoImage(self.imageV3)
        self.objImgV3 = self.CanevasJeu.create_image(self.Largeur, self.Hauteur // 2, image=self.imgV3)

        # Vaisseau pointe Gauche
        self.imageV4 = Image.open(os.getcwd() + "/IMAGES/ImagesF02/image-DestoyerImperial-3 Gauche.png")
        self.imageV4 = self.imageV4.resize((150, 180), Image.ANTIALIAS)
        self.imgV4 = PhotoImage(self.imageV4)
        self.objImgV4 = self.CanevasJeu.create_image(0, self.Hauteur // 2, image=self.imgV4)

        # Image Personnage : faucon millenium
        self.PersoImgVaisseau = Image.open(os.getcwd() + "/IMAGES/ImagesF02/faucon millenium-3.png")
        self.PersoImgVaisseau = self.PersoImgVaisseau.resize((30, 45), Image.ANTIALIAS)
        self.logo = PhotoImage(self.PersoImgVaisseau)
        self.ImgPerso = self.CanevasJeu.create_image(self.PosX, self.PosY, image=self.logo) # Placement à PosX et PosY
        # pour le déplacement de l'image comme personnage.

        # ...........< B U T T O N S >........................
        # ELEMENT GRAPHIQUE : <Button> = [Bouton B07] : Retour au menu (Retour F01)
        self.B07_retourMenu = Button(self, text="Retour Menu", command=self.commandeOuvreF01)
        self.B07_retourMenu.place(x=190, y=700)

        # ELEMENT GRAPHIQUE : <Button> = [A preciser] : Un bouton pour quitter l'application
        self.quitButton = Button(self, text="Quitter", command=self.destroy)
        self.quitButton.place(x=300, y=700)

        # ELEMENT GRAPHIQUE : <Button> = [Bouton B0?] : Fin de la partie et ouvre F04, temporaire ?
        self.B07_retourMenu = Button(self, text="Fin de partie", command=self.commandeOuvreF04)
        self.B07_retourMenu.place(x=400, y=700)

    # ==================================================
    # AUTRES FONCTIONS::::::::

    # ========================
    # FONCTION Récupérant l'angle du fichier score.txt et le retournant en radian. Auteur : Ethan SUISSA - Terminé
    def ValeurAngleParametreEnRadian(self):
        # Etape 1 : Récupération angle du fichier Score.txt.
        # A FAIRE QUAND BASE PRETE

        # Etape 2 : Conversion et envoi pour calcul commande programmable
        AngleEnDegree = 210  # Temporaire pour utiliser la commande programmable
        # Angles à tester : 26, 45, 60, 120, 210, 300, extremes (89, 179, 269, 359)
        print("Angle en degree = ", AngleEnDegree)  # Pour controle
        angleRadian = math.radians(AngleEnDegree)  # Conversion en radians pour calculs de com programmable
        return angleRadian

    # ========================
    # FONCTION OUTIL : Utilise l'équation de mouvement pour calculer la postion finale en fonction de l'angle
    # Auteur : Ethan SUISSA - Terminé
    def CalcProg(self, AngleDeduitDegree, Temps):
        v0 = 0.7  # Choix de vitesse intiale : modélise celle avec laquelle on lance un objet.
        g = 9.81  # Constante de gravitation influencant la chute.
        Angle_Deduit_Radian = math.radians(AngleDeduitDegree)  # convertion en Radian de l'angle deduit
        dx = v0 * cos(Angle_Deduit_Radian)  # modélise le déplacement horizontale avec les équations de mouvements :
        # utilisation de la dérivée de la position horizontale dx (vitesse).
        if Angle_Deduit_Radian == 0.0:  # Pour obtenir un déplacement horizontal d'un objet à la hauteur 0(pas de chute)
            g = 0
        dy = -g * Temps + v0 * sin(Angle_Deduit_Radian)  # modélise le déplacement verticale avec les équations de
        # mouvements : utilisation de la dérivée de la position horizontale dy (vitesse).
        # PRINCIPE GENERAL: dx et dy représentent les vitesses x et y de l'objet, c'est à dire son déplacement à un
        # temps donné, la fonction additionne donc à chaque étape de temps (elle est utilisée à chaque fois que le temps
        # augmente) la distance parcourue à la position.
        print("Angle radian:", Angle_Deduit_Radian)  # Test
        print("dx = :", dx, "dy = :", dy)  # Test
        return dx, dy

    # ========================
    # FONCTION OUTIL : Renvoie les valeurs de X et Y selon l'équation de mouvement et selon l'angle paramétré
    # Auteur : Ethan SUISSA - Terminé
    def ValeurPosXY(self, valX_Initial, valY_Initial, Temps):
        print("ValPosXY :  valXInitial =", valX_Initial) # Pour controle
        print("ValPosXY :  valYInitial =", valY_Initial) # Pour controle
        rebond = False # On considère qu'il n'y a pas de rebond au début.
        AngleEnDegree = degrees(self.ValeurAngleParametreEnRadian()) # Convertie l'angle retourné en radian en degrés
    # Ajustement de l'angle pour le quart de repère dans lequel on se trouve :
        # Bloc 1 = quart haut-droite
        if 0 <= AngleEnDegree <= 90:
            print("ValPosXY :  Bloc 1 ")  # pour controle
            Dx, Dy = self.CalcProg(AngleEnDegree, Temps) # Retourne les déplacement de x et y
            self.valX_Final = valX_Initial + Dx
            self.valY_Final = valY_Initial - Dy # Déplacement dans le sens du repère de l'écran : vers la droite pour X
            # avec l'addition et vers le haut pour Y avec la soustraction

        # Bloc 2 = quart haut-gauche
        if 90 < AngleEnDegree <= 180:
            print("ValPosX :  Bloc 2 ")  # pour controle
            Angle_Deduit_Degree = AngleEnDegree - 90 # Ajustement de l'angle pour celui des calculs de la trajectoire
            # dans le bloc 2.
            Dx, Dy = self.CalcProg(Angle_Deduit_Degree, Temps)
            self.valX_Final = valX_Initial - Dy # Soustraction au lieu d'addition pour X car déplacement horizontal vers
            # la gauche, inversion X et Y pour changement de repère.
            self.valY_Final = valY_Initial - Dx

        # Bloc 3 = quart bas-gauche
        if 180 < AngleEnDegree <= 270:
            print("ValPosX :  Bloc 3 ")  # pour controle
            Angle_Deduit_Degree = AngleEnDegree - 180
            Dx, Dy = self.CalcProg(Angle_Deduit_Degree, Temps)
            self.valX_Final = valX_Initial - Dx # Addition au lieu de soustraction pour X car déplacement horizontal
            # vers la gauche.
            self.valY_Final = valY_Initial + Dy  # Addition au lieu de soustraction pour Y car déplacement vertical
            # vers le bas.
            # inversion X et Y pour changement de repère.

        # Bloc 4 = quart bas-droite
        if 270 < AngleEnDegree <= 360:
            print("ValPosX :  Bloc 4  ")  # pour controle
            Angle_Deduit_Degree = AngleEnDegree - 270
            Dx, Dy = self.CalcProg(Angle_Deduit_Degree, Temps)
            self.valX_Final = valX_Initial + Dy
            self.valY_Final = valY_Initial + Dx # Addition au lieu de soustraction pour Y car déplacement vertical vers
            # le bas inversion X et Y pour changement de repère.

        print("ValPosXY : ValXFinal avant correction = ", self.valX_Final)
        print("ValPosXY : ValYFinal avant correction = ", self.valY_Final)

        # Correction de la position X si on sort du cadre
            # Rebond à droite
        if self.valX_Final > self.Largeur - self.Rayon:
            print("ValPosXY (posX):  Sortie du cadre à droite => Rebond ")
            self.valX_Final = valX_Initial - self.Rayon # Réajustement de la position X à celle juste avant
            rebond = True  # Marque le rebond pour ne pas rebondir indéfiniment (voir fonction "deplacement_P).

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
    # ========================
    # FONCTION OUTIL : Renvoie les valeurs de X et Y (pour commandes figées )selon l'équation de mouvement et selon
    # l'angle paramétré. Auteur : Lilandra ALBERT-LAVAUX - En cours

    def ValeurPosX(self, valInit, VarX):
        valPosX = valInit + VarX
        if valPosX > self.Largeur - self.Rayon or valPosX - self.Rayon < 0:
            valPosX = valInit - self.Rayon
        return valPosX

    def ValeurPosY(self,valInit, VarX):
        valPosY = valInit - VarX
        if valPosY < self.Rayon:
            valPosY = valInit + self.Rayon
        return valPosY


    # ========================
    # COMMANDE = ouvre F01,  (retour au menu)
    # Auteur : Ethan SUISSA - En Cours
    def commandeOuvreF01(self):
        # Ferme la fenetre
        self.destroy()  # ferme F02

        # Enregistre l'état du jeux et le score dans le fichier scores.txt:
        # >>>>>> ??A FAIRE

        # ouvre F01
        app = wF01.F01()
        app.mainloop()

    # ========================
    # COMMANDE = ouvre F01,  (retour au menu)
    # Auteur : Ethan SUISSA - En Cours
    def commandeOuvreF04(self):
        # Ferme la fenetre
        self.destroy()  # ferme F02

        # Enregistre l'état du jeux et le score dans le fichier scores.txt:
        # >>>>>> ??A FAIRE

        # ouvre F01
        app = wF04.F04()
        app.mainloop()

