# ======================================================
# PROJET TRANSVERSE 1 L1 : Jeu 2D Python
# Auteurs : Equipe ShirosakiBest = Ethan SUISSA, Lilandra ALBERT-LAVAULT, Pierre REY, Jean-Alexis TADDEI, Ludwig
# NEUBERTH- EFREI -L1 BN
# Date : 4 mai 2021 (?)
# Fichier F03 = "CONFIGURATION DES COMMANDES"
# ======================================================
from wF01 import *
import os
from tkinter import *
from PIL import Image
from PIL.ImageTk import PhotoImage



class F03(Tk):
    # Constructeur de l'objet F03 : ne pas supprimer !!!
    def __init__(self, IDJoueur):  # NomJoueur a ajouter en paramètre ?
        Tk.__init__(self)
        self.title("F03")  # Le titre de la fenêtre
        self.minsize(1200, 700)  # taille de fenêtre

        self.IdJoueur = IDJoueur # Transmission de l'ID du joueur
        self.Largeur = 1200  # Largeur de la zone de jeu
        self.Hauteur = 700  # Hauteur de la zone de jeu

        # Une méthode séparée pour construire le contenu de la fenêtre
        self.createWidgets()

    # Méthode de création des widgets
    def createWidgets(self):
        self.grid()  # Choix du mode d'arrangement des elements

        # ==================================================
        # FONCTIONS WIDGET ::::::::

        # ELEMENTS GRAPHIQUES ::::::::
        # Création des widgets (boutons, labels, etc...)
        self.PhotofondInfo = Image.open(os.getcwd() + "/IMAGES/ImageF03/ImageGuerreSatellite.jpg")
        self.PhotofondInfo = self.PhotofondInfo.resize((self.Largeur, self.Hauteur), Image.ANTIALIAS)  # resize permet
        # de mettre les photos au bon format pour les inclure dans le canevas. Antialias = inconnu, permet à resize de
        # fonctionner
        self.FondF01 = PhotoImage(self.PhotofondInfo)
        self.CanvasInfo = Canvas(self, width=self.Largeur, height=self.Hauteur)
        self.ImgFondF01 = self.CanvasInfo.create_image(self.Largeur // 2, self.Hauteur // 2, image=self.FondF01)
        self.CanvasInfo.pack(padx=5, pady=5)  # .pack sert à placer le texte
        self.CanvasInfo.tag_lower(self.ImgFondF01)


        # ...........< T E X T E S > .......................
        self.CanvasInfo.create_text(600, 350, text="Bienvenue dans notre jeu ! \nLe but est simple :"
                                          " esquivez les missiles qui vous arrivent dessus\n"
                                          "Pour cela, deux options s'offrent à vous :\n"
                                          "- La première est de se déplacer a l'aide des touches :\n "
                                            "'z' : pour aller en haut\t"
                                            "'q' : pour aller a gauche\n"
                                            "'s' : pour aller en bas\t"
                                            "'d' : pour aller à droite\n"
                                          "- La seconde est d'utiliser une commande programmable qui vous fera bondir\n"
                                          "avec un angle que vous pouvez choisir dans le menu, vous obtiendrez  \n"
                                          " un déplacement parabolique avec cet angle. '\n'"
                                          "La touche 'p' : vous permettra d'executer cette commande",
                           font='Gabriola 23 italic', fill='cyan')

        self.CanvasInfo.create_text(600, 50,
                                    text="Informations sur le jeu.", font='Gabriola 32 italic', fill='blue')
        # ==================================================


        # ...........< E N T R Y ' S > .......................


        # ...........< B U T T O N S >........................

        # ELEMENT GRAPHIQUE : <Button> = [Bouton B07 bis] : Retour au menu (Retour F01)
        self.RetourMenu = Button(self, text="Retourner au menu", command=self.commandeOuvreF01)
        self.RetourMenu.place(x=180, y=670)

        # ELEMENT GRAPHIQUE : <Button> = [A preciser] : Un bouton pour quitter l'application
        self.quitButton = Button(self, text="Quitter", command=self.destroy)
        self.quitButton.place(x=330, y=670)

    # ==================================================
    # AUTRES FONCTIONS DE LA CLASSE ::::::::

    # COMMANDE = ouvre F01,  (retour au menu)
    def commandeOuvreF01(self):
        # Ferme la fenetre
        self.destroy()  # ferme F03
        # ouvre F01
        app = F01(self.IdJoueur)
        app.mainloop()
