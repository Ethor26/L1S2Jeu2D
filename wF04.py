# ======================================================
# PROJET TRANSVERSE 1 L1 : Jeu 2D Python
# Auteurs : Equipe ShirosakiBest = Ethan SUISSA, Lilandra ALBERT-LAVAULT, Pierre REY, Jean-Alexis TADDEI, Ludwig
# NEUBERTH- EFREI -L1 BN
# Date : 4 mai 2021 (?)
# Fichier F04 = "RESULTATS DU JEUX"
# ======================================================
import os
from tkinter import *
import wF01
from Tools import *
from PIL import Image
from PIL.ImageTk import PhotoImage
import wF02


class F04(Tk):
    # Constructeur de l'objet F04 : ne pas supprimer !!!
    def __init__(self, Score, IdJoueur): # Importation du paramètre score de F02
        Tk.__init__(self)
        self.title("F04")  # Le titre de la fenêtre
        self.minsize(1200, 700)  # taille de fenêtre

        self.Largeur = 1200  # Largeur de la zone de résultat
        self.Hauteur = 700  # Hauteur de la zone de résultat

        self.ScoreRec = Score
        self.IDJoueur = IdJoueur
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
        # ...........< I M A G E S >.........................

        # Fond d'écran :
        self.PhotofondInfo = Image.open(os.getcwd() + "/IMAGES/ImageF04/ImageConflitSpace.jpg")
        self.PhotofondInfo = self.PhotofondInfo.resize((self.Largeur, self.Hauteur), Image.ANTIALIAS)  # resize permet
        # de mettre les photos au bon format pour les inclure dans le canevas. Antialias = inconnu, permet à resize de
        # fonctionner
        self.FondF04 = PhotoImage(self.PhotofondInfo)
        self.CanvasResult = Canvas(self, width=self.Largeur, height=self.Hauteur)
        self.ImgFondF04 = self.CanvasResult.create_image(self.Largeur // 2, self.Hauteur // 2, image=self.FondF04)
        self.CanvasResult.pack(padx=5, pady=5)  # .pack sert à placer le texte
        self.CanvasResult.tag_lower(self.ImgFondF04)

        # ...........< L A B E L S > .........................
        # ELEMENT GRAPHIQUE : <Label> = [A definir] : Afficher Score, nom, ...
        # >>>>> ??? plusieurs elements a faire !!!

        self.CanvasResult.create_text(600, 100,
                                      text="Résultat de la partie :", font='Gabriola 32 bold', fill='white')
        Depasse, BestScore = self.VictoireJeu()
        if Depasse:
            self.CanvasResult.create_text(300, 300,
                                       text="Bravo, vous avez battu votre record !\nVotre score est : {}\n"
                                            "Votre ancien meilleur score était : {}".format(
                                           self.ScoreRec, BestScore), font='Gabriola 26', fill='cyan')
        else:
            self.CanvasResult.create_text(300, 300,
                                         text="Dommage, vous ferez mieux la prochaine fois !\n Votre score est : {}\n"
                                              "Votre meilleur score est : {}".format(
                                             self.ScoreRec, BestScore), font='Gabriola 26', fill='cyan')

        # ...........< B U T T O N S >........................
        # ELEMENT GRAPHIQUE : <Button> = [Bouton B07 bis] : Retour au menu (Retour F01)
        self.RetourMenu = Button(self, text="Rejouer", command=self.commandeOuvreF02)
        self.RetourMenu.place(x=250, y=600)
        # ELEMENT GRAPHIQUE : <Button> = [A preciser] : Un bouton pour quitter l'application
        self.quitButton = Button(self, text="Quitter", command=self.destroy)
        self.quitButton.place(x=350, y=600)

    # ==================================================
    # AUTRES FONCTIONS::::::::

    # COMMANDE = Rejouer
    # >>>>> ??? 1 Faire !!!!
    # ===============================
    # FONCTIONS statuant si le meilleur score est dépassé (en cours).
    def VictoireJeu(self):
        tab, nbLignes = open_score_file2()
        if self.ScoreRec >= int(tab[self.IDJoueur+ 1][3]):
            print("Meilleur score dépassé")  # Pour controle
            return True, int(tab[self.IDJoueur+ 1][3])
        else:
            print("Meilleur score non atteint")  # Pour controle
            return False, int(tab[self.IDJoueur+ 1][3])

    # COMMANDE = ouvre F01,  (retour au menu)
    def commandeOuvreF01(self):
        # Ferme la fenetre
        self.destroy()  # ferme F04

        # ouvre F01
        app = wF01.F01(self.IDJoueur)
        app.mainloop()

# COMMANDE : ouvre F02 (Jouer)
    def commandeOuvreF02(self):
        self.destroy()  # ferme F01
        # ouvre F02
        app = wF02.F02(self.IDJoueur)         # implémente l'objet app
        app.focus_force()   # Force le focus sur la fenetre
        app.mainloop()