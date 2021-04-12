# ======================================================
# PROJET TRANSVERSE 1 L1 : Jeu 2D Python
# Auteurs : Equipe ShirosakiBest = Ethan SUISSA, Lilandra ALBERT-LAVAULT, Pierre REY, Jean-Alexis TADDEI, Ludwig
# NEUBERTH- EFREI -L1 BN
# Date : 4 mai 2021 (?)
# Fichier F00
# ======================================================
import os
from tkinter import * # Attention, TKinter doit être importé pour utiliser image de fond, pas remplacable par import de
# fichier wF0... De plus, ordre des import important !
from PIL import Image
from PIL.ImageTk import PhotoImage

from wF01 import F01


class F00(Tk):
    # Constructeur de l'objet F01 : ne pas supprimer, sert pour mettre les paramètres et fonctions propres à l'objet.
    def __init__(self, message):
        Tk.__init__(self)
        print("*** F00 ***") # Pour controle en console
        self.title("F00")  # Le titre de la fenêtre
        self.minsize(1200, 700)  # taille de fenêtre
        self.Largeur = 1200  # Largeur de la zone de jeu
        self.Hauteur = 700  # Hauteur de la zone de jeu

        # Une méthode séparée pour construire le contenu de la fenêtre
        self.createWidgets()

        print(message)  # A supprimer : controle/test de passage de valeur à la classe par son constructeur

    # Méthode de création des widgets
    def createWidgets(self):
        self.grid()  # Choix du mode d'arrangement

        # ...........< L A B E L S > .........................
        # ELEMENT GRAPHIQUE : <Label> = [Libellé T01] : ...??
        # ??? A FAIRE

        # Affichage du fond d'écran de F00
        self.Photofond = Image.open(os.getcwd() + "/IMAGES/Image F00/image5.png")
        self.FondF00 = PhotoImage(self.Photofond)
        self.CanvasPres = Canvas(self, width=self.Largeur, height=self.Hauteur)
        self.ImgFondF00 = self.CanvasPres.create_image(self.Largeur // 2, self.Hauteur // 2,image=self.FondF00)
        self.CanvasPres.pack(padx=5, pady=5)  # .pack sert à placer le texte
        self.CanvasPres.tag_lower(self.ImgFondF00)

        # Affichage du scénario : un label sur Tkinter permet d'afficher du texte, create_text met du texte dans un
        # canvas. Paramètre inutile ici car placement direct.
        self.CanvasPres.create_text(600, 300,
                                    text="Il y a bien longtemps, une galaxie lointaine était dirigée par un Conseil"
                                         " de sages qui s’efforçaient à ce que tous le monde vive une vie paisible.\n"
                                         "Malheureusement, ils virent bientôt apparaître une armée menée par un"
                                         " empereur infecté par un virus nommé Galacticov. Ce virus avait paralysé\n"
                                         "toutes les zones du cerveau de l’empereur qui lui permettait d’éprouver"
                                         " des émotions négatives et stimulé les connexions dans celles créant des\n"
                                         "émotions négatives. Un empereur juste et intègre devint alors cruel et "
                                         "implacable. Ce virus étant contrôlé à distance par un conseiller avide\n "
                                         " de pouvoir dans une centrale, le Conseil vous recruta avec d’autres héros"
                                         " pour atteindre et détruire cette centrale, en évitant les tirs des "
                                         "vaisseaux\n "
                                         "délégué par l’empereur. Vous devrez donc passer à travers "
                                         "cette armée, mais avec l’interdiction du Conseil de détruire les autres "
                                         "vaisseaux.\n "
                                         "En effet, ils sont contrôlés par des pilotes innocents mais manipulés. Ils "
                                         "ignorent "
                                         "vos objectifs et s’imaginent que vous venez détruire leur empire.\n " 
                                         "Une quête ardue commence alors pour vous…\n", font='Gabriola 17 italic', fill='white')
        self.CanvasPres.create_text(600, 50,
                                    text="Un heros Contre Galacticov.", font='Gabriola 32 italic', fill='cyan')

        # ELEMENT GRAPHIQUE : <Label> = [Libellé T02] : ...??
        # ??? A FAIRE

        # ELEMENT GRAPHIQUE : <Label> = [Libellé T03] : ...??
        # ??? A FAIRE
        # ...........

        # ...........< B U T T O N S >........................
        # ELEMENT GRAPHIQUE : <Button> = [Bouton B01] : ouvrir menu (F01)
        self.ouvreF01 = Button(self, text="Start", command=self.commandeOuvreF01)
        self.ouvreF01.place(x=200, y=650)

        # ELEMENT GRAPHIQUE : <Button> = [A preciser] : Un bouton pour quitter l'application
        self.quitButton = Button(self, text="Quitter", command=self.destroy)
        self.quitButton.place(x=300, y=650)

    # ==================================================
    # Autres Fonctions :

    # COMMANDE = ouvre F01,  et ferme F00 (retour au menu)
    def commandeOuvreF01(self):
        self.destroy()  # ferme F00
        # ouvre F01
        app = F01(0) # 0 représente un ID nul, sert pour que F01 puisse transmettre l'ID après
        app.mainloop()
