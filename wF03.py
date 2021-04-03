# ======================================================
# PROJET TRANSVERSE 1 L1 : Jeu 2D Python
# Auteurs : Equipe ShirosakiBest = Ethan SUISSA, Lilandra ALBERT-LAVAULT, Pierre REY, Jean-Alexis TADDEI, Ludwig
# NEUBERTH- EFREI -L1 BN
# Date : 4 mai 2021 (?)
# Fichier F03 = "CONFIGURATION DES COMMANDES"
# ======================================================
from tkinter import *
import wF01
from Tools import *


class F03(Tk):
    # Constructeur de l'objet F03 : ne pas supprimer !!!
    def __init__(self):  # NomJoueur a ajouter en paramètre ?
        Tk.__init__(self)
        self.title("F03")  # Le titre de la fenêtre
        self.minsize(1200, 700)  # taille de fenêtre
        # Une méthode séparée pour construire le contenu de la fenêtre
        self.createWidgets()

    # Méthode de création des widgets
    def createWidgets(self):
        self.grid()  # Choix du mode d'arrangement des elements

        # ==================================================
        # FONCTIONS WIDGET ::::::::
        def EnregistrAngle():  # Fonction doit être mise avant sinon erreur
            TextAngleEnDegree = entreAngle.get()
            # Etape 1 : Ajustement de l'angle pour un résultat convenable.
            AngleEnDegree = TrtAngle(TextAngleEnDegree)
            print("Angle en degree = ", AngleEnDegree)  # Pour controle

            # Etape 2 : Envoi de l'angle dans score.txt
            ajout_angle_F02(AngleEnDegree)

        def TrtAngle(TextAngleEnDegree):
            # Récupération angle de la zone de Saisie ou pose de 0
            AngleEnDegree = 0
            msg = "..."
            if TextAngleEnDegree != "":
                try: # Essai la tranformation en int en vérifiant les erreurs avant (pour éviter un plantage total).
                    AngleEnDegree = int(TextAngleEnDegree)
                except ValueError:
                    msg = ">> Angle doit etre un entier "  # Message informant l'utilisateur, s'affiche à l'ecran
                    print(msg)  # Pour contrôle en console
            if AngleEnDegree >= 360 or AngleEnDegree <= -360:
                AngleEnDegree = AngleEnDegree % 360 # Création d'un modulo pour ajuster les angles trop grand.
            if AngleEnDegree < 0:
                AngleEnDegree += 360  # Angle ne change pas mais on le replace sur l'intervalle [0; 360]
            self.messageUtilisateurAngle.set(msg)  # Pour mise à jour texte écran
            print(str(self.messageUtilisateurAngle.get()))  # Pour Controle
            return AngleEnDegree

        # ==================================================
        # ELEMENTS GRAPHIQUES ::::::::
        # Création des widgets (boutons, labels, etc...)
        # ...........< T E X T E S > .......................
        # ELEMENT GRAPHIQUE : <Texte> = [à definir] annoncant la saisie de l'angle # A REPOSITIONNER !!!
        lblEntreAngle = Label(self, text="Angle=")  # Nom de la fenêtre en rouge à déclarer comme au dessus (avec le nom
        # de fenêtre qu'on veut
        lblEntreAngle.place(x=150, y=200)

        # ...........< E N T R Y ' S > .......................
        # ELEMENT GRAPHIQUE : <Entry> = [à definir] pour saisir l'angle # A REPOSITIONNER !!!

        entreAngle = Entry(self)  # Ajouter self pour mettre dans constructeur ?
        entreAngle.place(x=200, y=200, width=70)  # A placer à coté du bouton "Appliquer", écart de 50 entre les x
        # Variable(s)
        self.messageUtilisateurAngle = StringVar()  # Variable de message d'erreur de saisie type stringvar() pour
        # maj Label
        self.messageUtilisateurAngle.set("...")
        # pertinent.

        # ...........< B U T T O N S >........................

        # ELEMENT GRAPHIQUE : <Button> = [Bouton B09] : "Appliquer (Enregistrer) l'angle"
        # >>>>> ??? a faire
        self.AppliqAngle = Button(self, text="Appliquer l'angle", command=EnregistrAngle)
        self.AppliqAngle.place(x=250, y=200)

        # ELEMENT GRAPHIQUE : <Button> = [Bouton B07 bis] : Retour au menu (Retour F01)
        self.B07_retourMenu = Button(self, text="Retour Menu", command=self.commandeOuvreF01)
        self.B07_retourMenu.place(x=10, y=600)

        # ELEMENT GRAPHIQUE : <Button> = [A preciser] : Un bouton pour quitter l'application
        self.quitButton = Button(self, text="Quitter", command=self.destroy)
        self.quitButton.place(x=150, y=600)

        # ELEMENT GRAPHIQUE : <Label> = Message
        self.LblMessage = Label(self, textvariable=self.messageUtilisateurAngle)
        self.LblMessage.place(x=150, y=250)

    # ==================================================
    # AUTRES FONCTIONS DE LA CLASSE ::::::::

    # COMMANDE = ouvre F01,  (retour au menu)
    def commandeOuvreF01(self):
        # Ferme la fenetre
        self.destroy()  # ferme F03
        # ouvre F01
        app = wF01.F01()
        app.mainloop()
