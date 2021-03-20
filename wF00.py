# ======================================================
# PROJET TRANSVERSE 1 L1 : Jeu 2D Python
# Auteurs : Equipe ShirosakiBest = Ethan SUISSA, Lilandra ALBERT-LAVAULT, Pierre REY, Jean-Alexis TADDEI, Ludwig
# NEUBERTH- EFREI -L1 BN
# Date : 4 mai 2021 (?)
# Fichier F00
# ======================================================
from tkinter import *
from wF01 import F01

class F00(Tk):
    # Constructeur de l'objet F01 : ne pas supprimer !!!
    def __init__(self, message):
        Tk.__init__(self)
        self.configure(background='black')  # backgroud fenêtre
        self.title("F00")  # Le titre de la fenêtre

        self.minsize(1200, 700)  # taille de fenêtre

        # Une méthode séparée pour construire le contenu de la fenêtre
        self.createWidgets()

        print(message)  # A supprimer : controle/test de passage de valeur à la classe par son constructeur

    # Méthode de création des widgets
    def createWidgets(self):
        self.grid()  # Choix du mode d'arrangement

        # Création des widgets :

        # ...........< L A B E L S > .........................
        # ELEMENT GRAPHIQUE : <Label> = [Libellé T01] : ...??
        # ??? A FAIRE

        # Affichagage du sénario

        lbl = Label(self, text="Il y a bien longtemps, une galaxie lointaine était dirigée par un Conseil\n"
                               "de sages qui s’efforçaient à ce que tous le monde vive une vie paisible.\n"
                               "Malheureusement, ils virent bientôt apparaître une armée menée par un\n"
                               "empereur infecté par un virus nommé Galacticov. Ce virus avait paralysé\n"
                               "toutes les zones du cerveau de l’empereur qui lui permettait d’éprouver\n"
                               "des émotions négatives et stimulé les connexions dans celles créant des\n"
                               "émotions négatives. Un empereur juste et intègre devint alors cruel et\n "
                               "implacable.Ce virus étant contrôlé à distance par un conseiller avide\n "
                               "de pouvoir dans une centrale, le Conseil vous recruta avec d’autres héros\n"
                               "pour atteindre et détruire cette centrale, en évitant les tirs des vaisseaux\n"
                               "délégué par l’empereur. Vous, <Nom à définir>, devrez donc passer à travers \n"
                               "cette armée, mais avec l’interdiction du Conseil de détruire les autres vaisseaux.\n"
                               "En effet, ils sont contrôlés par des pilotes innocents mais manipulés. Ils ignorent\n"
                               "vos objectifs et s’imaginent que vous venez détruire leur empire. Une quête ardue \n"
                               "commence pour vous…\n", font='Arial 21 bold', bg='black', fg='white', height=21, width=78)
        lbl.pack(padx=5, pady=5)
        # .pack sert à placer le texte
        # ELEMENT GRAPHIQUE : <Label> = [Libellé T02] : ...??
        # ??? A FAIRE

        # ELEMENT GRAPHIQUE : <Label> = [Libellé T03] : ...??
        # ??? A FAIRE
        # ...........

        # ...........< B U T T O N S >........................
        # ELEMENT GRAPHIQUE : <Button> = [Bouton B01] : ouvrir menu (F01)
        self.ouvreF01 = Button(self, text="Start", command=self.commandeOuvreF01)
        self.ouvreF01.place(x=10, y=600)

        # ELEMENT GRAPHIQUE : <Button> = [A preciser] : Un bouton pour quitter l'application
        self.quitButton = Button(self, text="Quitter", command=self.destroy)
        self.quitButton.place(x=150, y=600)

    # ==================================================
    # D'autres méthodes :
    # ==================================================

    # COMMANDE = ouvre F01,  et ferme F00 (retour au menu)
    def commandeOuvreF01(self):
        self.destroy()  # ferme F00
        # ouvre F01
        app = F01()  #
        app.mainloop()
