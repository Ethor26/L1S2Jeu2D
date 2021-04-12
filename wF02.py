# ======================================================
# PROJET TRANSVERSE 1 L1 : Jeu 2D Python
# Auteurs : Equipe ShirosakiBest = Ethan SUISSA, Lilandra ALBERT-LAVAULT, Pierre REY, Jean-Alexis TADDEI, Ludwig
# NEUBERTH- EFREI -L1 BN
# Date : 4 mai 2021 (?)
# Fichier F02 = "JEUX EN ACTION"
# ======================================================
from math import *
import os
from tkinter import *
from PIL import Image
from PIL.ImageTk import PhotoImage
from Tools import *
import wF01  # Modification de l'import pour éviter les "circular import", en général rajoute des "wF01.Tk"
from wF04 import F04


class F02(Tk):
    # Constructeur de l'objet F02 : ne pas supprimer !!!
    def __init__(self, IDJoueur):
        Tk.__init__(self)
        self.title("F02")  # Le titre de la fenêtre
        self.minsize(1200, 700)  # taille de fenêtre

        self.IdJoueur = IDJoueur

        # Une méthode séparée pour construire le contenu de la fenêtre
        self.Largeur = 1200  # Largeur de la zone de jeu
        self.Hauteur = 680  # Hauteur de la zone de jeu

        # Dimension de l'image du vaisseaux
        self.Perso_Hauteur = 45
        self.Perso_Largeur = 30

        # position initiale du perso, respectivement X et Y
        self.PosX = 600
        self.PosY = 400

        # Temps initiaux
        self.Temps = 0
        self.cpTemps = 2
        self.LimiteTpsDepl = 5

        # Score Initial
        self.Score = 0

        # 1ere position finale (confondue avec initiale)
        self.valY_Final = 0
        self.valX_Final = 0

        self.Score = 1
        # Nombre de Pas de déplacement
        self.NbPas = 20

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

            # Si touche d => deplt a droite
            if self.touche == 'd':
                print("Info:  touche d activée ***")
                deplacement_D()

            # Si touche q => deplt a Gauche
            if self.touche == 'q':
                print("Info:  touche q activée ***")
                deplacement_Q()

            # Si touche s => deplt a bas
            if self.touche == 's':
                print("Info:  touche s activée ***")
                deplacement_S()

            # Si touche z => deplt a Haut
            if self.touche == 'z':
                print("Info:  touche z activée ***")
                deplacement_Z()

            # Si touche p => déplacement selon equation de mouvement
            if self.touche == 'p':
                print("Info:  touche p activée ***")
                deplacement_P()

        # =============================================================================
        # FONCTION de déplacement de la touche P. Auteur : Ethan SUISSA - Terminé
        def deplacement_P():
            nbRebond = 0  # Initialisation du nombre de rebond sur les côtés à chaque mouvement
            self.Temps += 0.00015  # Augmentation d'une variable de temps pour calcul Position Y (de commande
            # programmable) et permet de définir la limite du mouvement.
            # Récupération des nouvelles position
            self.PosX, self.PosY, self.siRebond, Temps = self.ValeurPosXY_P(self.PosX, self.PosY, self.Temps)

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

        # =============================================================================
        # FONCTION de déplacement de la touche D. Auteur : Lilandra ALBERT-LAVAUX - Terminé
        def deplacement_D():  # ATTENTION : Pas de paramètres !
            nbRebond = 0  # Initialisation du nombre de rebond sur les côtés à chaque mouvement

            # Récupération de la nouvelle position de X et renvoie siRebond=true si on touche le bord
            self.PosX, self.siRebond = self.ValeurPosX(self.PosX, self.NbPas)

            print("Deplacement Droite : posY = ", self.PosY)  # pour controle
            print("Deplacement Droite : posX = ", self.PosX)  # pour controle

            # Repositionnne le personnage
            self.CanevasJeu.coords(self.ImgPerso, self.PosX, self.PosY)

            # S'il y a un rebond sur un côté, augmente la variable du nombre de rebond
            if self.siRebond:
                nbRebond = nbRebond + 1
                print("Nombre de rebond = ", nbRebond)

            # On déclenche le déplacement toute les 40 ms, réactualisation de la fenêtre
            idAfter = self.after(40, deplacement_D)

            # On arrête le dépldacement s'il y a un rebond ou si on arrive à la limite du temps de déplacement
            self.cpTemps += 1

            if nbRebond > 0 or self.cpTemps > self.LimiteTpsDepl:
                self.after_cancel(idAfter)
                self.cpTemps = 0

        # =============================================================================
        # FONCTION de déplacement de la touche Q. Auteur : Lilandra ALBERT-LAVAUX - Terminé
        def deplacement_Q():  # ATTENTION : Pas de paramètres !
            nbRebond = 0  # Initialisation du nombre de rebond sur les côtés à chaque mouvement

            # Récupération de la nouvelle position de X et renvoie siRebond=true si on touche le bord
            self.PosX, self.siRebond = self.ValeurPosX(self.PosX, -self.NbPas)
            print("Deplacement Gauche : posY = ", self.PosY)  # pour controle
            print("Deplacement Gauche : posX = ", self.PosX)  # pour controle

            # Repositionnne le personnage
            self.CanevasJeu.coords(self.ImgPerso, self.PosX, self.PosY)

            # S'il y a un rebond sur un côté, augmente la variable du nombre de rebond
            if self.siRebond:
                nbRebond = nbRebond + 1
                print("Nombre de rebond = ", nbRebond)

            # On déclenche le déplacement toute les 40 ms, réactualisation de la fenêtre
            idAfter = self.after(40, deplacement_Q)

            # On arrête le dépldacement s'il y a un rebond ou si on arrive à la limite du temps de déplacement
            self.cpTemps += 1

            if nbRebond > 0 or self.cpTemps > self.LimiteTpsDepl:
                self.after_cancel(idAfter)
                self.cpTemps = 0

        # =============================================================================
        # FONCTION de déplacement de la touche Z. Auteur : Lilandra ALBERT-LAVAUX - Terminé
        def deplacement_Z():  # ATTENTION : Pas de paramètres !
            nbRebond = 0  # Initialisation du nombre de rebond sur les côtés à chaque mouvement

            # Récupération de la nouvelle position de X et renvoie siRebond=true si on touche le bord
            self.PosY, self.siRebond = self.ValeurPosY(self.PosY, -self.NbPas)

            print("Deplacement Haut : posY = ", self.PosY)  # pour controle
            print("Deplacement Haut : posX = ", self.PosX)  # pour controle

            # Repositionnne le personnage
            self.CanevasJeu.coords(self.ImgPerso, self.PosX, self.PosY)

            # S'il y a un rebond sur un côté, augmente la variable du nombre de rebond
            if self.siRebond:
                nbRebond = nbRebond + 1
                print("Nombre de rebond = ", nbRebond)

            # On déclenche le déplacement toute les 40 ms, réactualisation de la fenêtre
            idAfter = self.after(40, deplacement_Z)

            # On arrête le dépldacement s'il y a un rebond ou si on arrive à la limite du temps de déplacement
            self.cpTemps += 1

            if nbRebond > 0 or self.cpTemps > self.LimiteTpsDepl:
                self.after_cancel(idAfter)
                self.cpTemps = 0

        # =============================================================================
        # FONCTION de déplacement de la touche S. Auteur : Lilandra ALBERT-LAVAUX - Terminé
        def deplacement_S():  # ATTENTION : Pas de paramètres !
            nbRebond = 0  # Initialisation du nombre de rebond sur les côtés à chaque mouvement

            # Récupération de la nouvelle position de X et renvoie siRebond=true si on touche le bord
            self.PosY, self.siRebond = self.ValeurPosY(self.PosY, self.NbPas)

            print("Deplacement Bas : posY = ", self.PosY)  # pour controle
            print("Deplacement Bas : posX = ", self.PosX)  # pour controle

            # Repositionnne le personnage
            self.CanevasJeu.coords(self.ImgPerso, self.PosX, self.PosY)

            # S'il y a un rebond sur un côté, augmente la variable du nombre de rebond
            if self.siRebond:
                nbRebond = nbRebond + 1
                print("Nombre de rebond = ", nbRebond)

            # On déclenche le déplacement toute les 40 ms, réactualisation de la fenêtre
            idAfter = self.after(40, deplacement_S)

            # On arrête le dépldacement s'il y a un rebond ou si on arrive à la limite du temps de déplacement
            self.cpTemps += 1

            if nbRebond > 0 or self.cpTemps > self.LimiteTpsDepl:
                self.after_cancel(idAfter)
                self.cpTemps = 0

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
                                                            image=self.imgfondEcran)  # Implémentation de l'image dans le
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
        self.imgV1 = PhotoImage(self.imageV1)  # Même principe que fond d'écran
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
        self.PersoImgVaisseau = self.PersoImgVaisseau.resize((self.Perso_Largeur, self.Perso_Hauteur), Image.ANTIALIAS)
        self.logo = PhotoImage(self.PersoImgVaisseau)
        self.ImgPerso = self.CanevasJeu.create_image(self.PosX, self.PosY, image=self.logo)  # Placement à PosX et PosY
        # pour le déplacement de l'image comme personnage.

        # ...........< B U T T O N S >........................
        # ELEMENT GRAPHIQUE : <Button> = [Bouton B07] : Retour au menu (Retour F01)
        self.B07_retourMenu = Button(self, text="Retour Menu", command=self.commandeOuvreF01)
        self.B07_retourMenu.place(x=190, y=700)

        # ELEMENT GRAPHIQUE : <Button> = [A preciser] : Un bouton pour quitter l'application
        self.quitButton = Button(self, text="Quitter", command=self.destroy)
        self.quitButton.place(x=300, y=700)

        # ELEMENT GRAPHIQUE : <Button> = [Bouton B0?] : Fin de la partie et ouvre F04, temporaire ?
        self.B07_retourMenu = Button(self, text="Fin de partie", command=self.Fin_Partie)
        self.B07_retourMenu.place(x=400, y=700)

    # ========================
    # FONCTION OUTILS : Récupérant l'angle du fichier score.txt et le retournant en radian. Auteur : Ethan SUISSA - Terminé
    def ValeurAngleParametreEnRadian(self):
        # Etape 1 : Récupération angle du fichier Score.txt.
        tab, nbLignes = open_score_file2()
        VAngleEnDegree = int(tab[self.IdJoueur + 1][2])  # self.IdJoueur + 2 = Numéro de ligne, on enlève 1 car tableau.

        # Etape 2 : Conversion et envoi pour calcul commande programmable
        # Angles à tester : 26, 45, 60, 120, 210, 300, extremes (89, 179, 269, 359)
            # Angle Temporaire
        # AngleEnDegree = 269
        # print("Angle en degree = ", AngleEnDegree)  # Pour controle
        # angleRadian = math.radians(AngleEnDegree)  # Conversion en radians pour calculs de com programmable
        # return angleRadian
            # Vrai Angle
        print("Angle en degree = ", VAngleEnDegree)
        VangleRadian = radians(VAngleEnDegree)
        return VangleRadian

    # ========================
    # FONCTION OUTIL : Utilise l'équation de mouvement pour calculer la postion finale en fonction de l'angle
    # Auteur : Ethan SUISSA - Terminé
    def CalcProg(self, AngleDeduitDegree, Temps):
        v0 = 0.7  # Choix de vitesse intiale : modélise celle avec laquelle on lance un objet.
        g = 9.81  # Constante de gravitation influencant la chute.
        Angle_Deduit_Radian = radians(AngleDeduitDegree)  # convertion en Radian de l'angle deduit, utiliser
        # math.radians si "import math"
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
    # FONCTION OUTIL : Utilisé pour la touche programmable exclusivement.
    # Renvoie les valeurs de X et Y selon l'équation de mouvement et selon l'angle paramétré
    # Auteur : Ethan SUISSA - Terminé
    def ValeurPosXY_P(self, valX_Initial, valY_Initial, Temps):
        print("ValPosXY :  valXInitial =", valX_Initial)  # Pour controle
        print("ValPosXY :  valYInitial =", valY_Initial)  # Pour controle
        AngleEnDegree = degrees(self.ValeurAngleParametreEnRadian())  # Convertie l'angle retourné en radian en degrés

        # Ajustement de l'angle pour le quart de repère dans lequel on se trouve :
        # Bloc 1 = quart haut-droite
        if 0 <= AngleEnDegree <= 90:
            print("ValPosXY :  Bloc 1 ")  # pour controle
            Dx, Dy = self.CalcProg(AngleEnDegree, Temps)  # Retourne les déplacement de x et y
            self.valX_Final = valX_Initial + Dx
            self.valY_Final = valY_Initial - Dy  # Déplacement dans le sens du repère de l'écran : vers la droite pour X
            # avec l'addition et vers le haut pour Y avec la soustraction

        # Bloc 2 = quart haut-gauche
        if 90 < AngleEnDegree <= 180:
            print("ValPosX :  Bloc 2 ")  # pour controle
            Angle_Deduit_Degree = AngleEnDegree - 90  # Ajustement de l'angle pour celui des calculs de la trajectoire
            # dans le bloc 2.
            Dx, Dy = self.CalcProg(Angle_Deduit_Degree, Temps)
            self.valX_Final = valX_Initial - Dy  # Soustraction au lieu d'addition pour X car déplacement horizontal vers
            # la gauche, inversion X et Y pour changement de repère.
            self.valY_Final = valY_Initial - Dx

        # Bloc 3 = quart bas-gauche
        if 180 < AngleEnDegree <= 270:
            print("ValPosX :  Bloc 3 ")  # pour controle
            Angle_Deduit_Degree = AngleEnDegree - 180
            Dx, Dy = self.CalcProg(Angle_Deduit_Degree, Temps)
            self.valX_Final = valX_Initial - Dx  # Addition au lieu de soustraction pour X car déplacement horizontal
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
            self.valY_Final = valY_Initial + Dx  # Addition au lieu de soustraction pour Y car déplacement vertical vers
            # le bas inversion X et Y pour changement de repère.

        print("ValPosXY : ValXFinal avant correction = ", self.valX_Final)
        print("ValPosXY : ValYFinal avant correction = ", self.valY_Final)

        # Correction de la position X si on sort du cadre
        # Rebond à gauche ou à droite
        rebondL = self.RebondLargeur(valX_Initial)
        rebondH = self.RebondHauteur(valY_Initial)
        if rebondL or rebondH:
            rebond = True
        else:
            rebond = False
        return self.valX_Final, self.valY_Final, rebond, Temps

    # ========================
    # FONCTION OUTIL : Vérifient si il y a eu un rebond, si oui, envoient une confirmation avec un booléen. La première
    # gère ceux à gauche ou à droite, et la 2e ceux en haut ou en bas. Auteur : Ethan SUISSA - Terminé

    def RebondLargeur(self, valX_Initial):
        rebond = False  # On considère qu'il n'y a pas de rebond au début.
        # Rebond à droite
        if self.valX_Final > self.Largeur - self.Perso_Largeur + 20:  # -20 ou -20 Pour précision du rebond
            print("ValPosXY (posX):  Sortie du cadre à droite => Rebond ")
            self.valX_Final = valX_Initial - self.Perso_Largeur + 20  # Réajustement de la position X à celle juste avant
            rebond = True  # Marque le rebond pour ne pas rebondir indéfiniment (voir fonction "deplacement_P).

            # Rebond à gauche
        if self.valX_Final < self.Perso_Largeur - 20:
            print("ValPosXY (posX):  Sortie du cadre à gauche => Rebond ")
            self.valX_Final = valX_Initial + self.Perso_Largeur - 20
            rebond = True
        return rebond

    def RebondHauteur(self, valY_Initial):
        rebond = False  # On considère qu'il n'y a pas de rebond au début.
        # Rebond en bas
        if self.valY_Final < self.Perso_Hauteur - 30:  # -30 ou +30 Pour précision du rebond
            print("ValPosXY (posY):  Sortie en bas ==> Rebond")
            self.valY_Final = valY_Initial + self.Perso_Hauteur - 30
            rebond = True
            # Rebond en haut
        if self.valY_Final > self.Hauteur - self.Perso_Hauteur + 30:
            print("ValPosXY (posY):  Sortie en haut ==> Rebond")
            self.valY_Final = valY_Initial - self.Perso_Hauteur + 30
            rebond = True
        return rebond

    # ========================
    # FONCTION OUTIL : Renvoie les valeurs de X et Y pour commandes figées. Auteur : Lilandra ALBERT-LAVAUX - Terminé

    def ValeurPosX(self, valInit, VarX):
        self.valX_Final = valInit + VarX  # On crée la nouvelle position de X en aditionnant son ancienne position avec
        # le décalage sur les cotés (vers la droite ou la gauche).
        rebond = self.RebondLargeur(valInit)  # On teste le rebond sur les côtés avec la fonction RebondLargeur.
        return self.valX_Final, rebond  # Renvoie des paramètres aux fonctions de déplacement pour réutilisation.

    def ValeurPosY(self, valInit, VarY):
        self.valY_Final = valInit + VarY  # On crée la nouvelle position de Y en aditionnant son ancienne position avec
        # le décalage de hauteur (vers le haut ou le bas).
        rebond = self.RebondHauteur(valInit)  # On teste le rebond sur les côtés avec la fonction RebondHauteur.
        return self.valY_Final, rebond  # Renvoie des paramètres aux fonctions de déplacement pour réutilisation.

    # ========================
    # COMMANDE = ouvre F01,  (retour au menu)
    # Auteur : Ethan SUISSA - En Cours
    def commandeOuvreF01(self):
        # Ferme la fenetre
        self.destroy()  # ferme F02

        # Enregistre l'état du jeux et le score dans le fichier scores.txt:
        # >>>>>> ??A FAIRE

        # ouvre F01
        app = wF01.F01(self.IdJoueur)
        app.mainloop()

    # ========================
    # COMMANDE = ouvre F04,  Fenêtre de résultat de la partie
    # Auteur : Ethan SUISSA - En Cours
    def commandeOuvreF04(self):
        # Ferme la fenetre
        F02.destroy(self)  # ferme F02, format donne même résultat
        # ouvre F01
        app = F04(self.Score, self.IdJoueur)
        app.mainloop()

        # Enregistre l'état du jeux et le score dans le fichier scores.txt:
        # >>>>>> ??A FAIRE

    # ========================
    # FONCTION : Fonction de fin de partie, appelée si partie finie pour récupérer le meilleur score et ouvrir F04
    def Fin_Partie(self):
        self.Score = 3216  # A récupérer
        BestScore = score_comparaison2(self.Score, self.IdJoueur)  # Ligne trouvée avec l'ID dans la fonction
        ModifPrecisFichier(self.IdJoueur + 2, 3, BestScore)  # self.IdJoueur +2 car c'est le numéro de ligne
        # correspondant, le meilleur score est à l'emplacement t[i][3] du tableau d'"open_score_file",
        # BestScore est ce qu'on écrit.
        self.commandeOuvreF04()
