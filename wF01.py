# ======================================================
# PROJET TRANSVERSE 1 L1 : Jeu 2D Python
# Auteurs : Equipe ShirosakiBest = Ethan SUISSA, Lilandra ALBERT-LAVAULT, Pierre REY, Jean-Alexis TADDEI, Ludwig
# NEUBERTH- EFREI -L1 BN
# Date : 4 mai 2021 (?)
# Fichier F01 = "ECRAN D'ACCUEIL"

# ======================================================
from tkinter import *

from Tools import *
#from wF02 import F02
#from wF03 import F03
from wF02 import F02
from wF03 import F03


class F01(Tk):

    # Constructeur de l'objet F01 : ne pas supprimer !!!
    def __init__(self, IDJoueur):
        Tk.__init__(self)
        print("*** F01 ***") # Pour controle en console
        self.title("F01")  # Le titre de la fenêtre
        self.minsize(1200, 700)  # taille de fenêtre

        self.IdJoueur = IDJoueur
        self.createWidgets() # Une méthode séparée pour construire le contenu de la fenêtre : A PLACER EN BAS
    # Méthode/fonction de création des widgets
    def createWidgets(self):
        self.grid()  # Choix du mode d'arrangement

        # FONCTION Récupération Nom et enregistrement dans score.txt
        def RecupNameDever():
            "Enregistrer le ,nom"
            Name = EntreeNom.get()
            print("Nom :", Name)
            msg = "En Avant !"
            if Name != "": # Si la fenêtre d'entrée du nom n'est pas vide :
                # On vérifie si le joueur existe dans la base de donnée
                tab, NbLignes = open_score_file2()
                JoueurExist = False
                for i in range(NbLignes):
                    if tab[i][1] == Name:
                        JoueurExist = True
                        self.IdJoueur = i - 1 # L'id du joueur est toujours égal à la valeur du numéro de ligne - 2 mais
                        # on rajoute 1 pour le décalage du tableau
                        break
                # Si le joueur n'existe pas, on initialise son profil
                if not JoueurExist:
                    # Ajout du nom dans la base
                    ajout_nom_F000(Name)   # A configurer pour pas à faire à chaque fois
                    ajout_angle_F02(0)
                    ajout_score_F0(0)    # Angle et meilleur score sont à 0 car nouveau profil
                    self.IdJoueur = NbLignes - 1   # -1 l'ID est à la ligne NbLignes-1, on ajoute aussi le décalage
                    # de -2.
                    # Déverouillage des boutons
                    #                 # ELEMENT GRAPHIQUE : <Button> = [Bouton B0?] : Configuration commande
                BoutConfCom = Button(self, text="Configuration Commandes", command=self.commandeOuvreF03)
                BoutConfCom.place(x=10, y=250)  # Bouton pour tester le verrouillage
                                    # Bouton "Jouer" à placer
                self.ouvreF02 = Button(self, text="jouer", command=self.commandeOuvreF02)
                self.ouvreF02.place(x=10, y=600)
            else:
                msg = "Pas de nom, pas de jeu !"
            self.messageUtilisateurNom.set(msg)  # Pour mise à jour texte écran


    # ==================================================
    # ELEMENTS GRAPHIQUES::::::::

        # ...........< L A B E L S > .........................
        # ELEMENT GRAPHIQUE : <Label> = [Libellé T04] : ...??
        # ??? A FAIRE

        # ELEMENT GRAPHIQUE : <Label> = [Libellé T05] : ...??
        # ??? A FAIRE

        # ELEMENT GRAPHIQUE : <Label> = [Libellé T06] : ...??
        # ??? A FAIRE

        # ELEMENT GRAPHIQUE : <Label> = [Libellé T07] : ...??
        # ??? A FAIRE

        # ELEMENT GRAPHIQUE : <Label> = [Libellé T08] : ...??
        # ??? A FAIRE


        # Création d'un widget Label (texte 'Nom')
        Label1 = Label(self, text='Quel est ton nom ', font=("Arial", 20)) # ajouter: "jeune protecteur de la Galaxie?"
        # Label1.pack(padx=1, pady=1)
        Label1.place(x=10, y=50)


        # ...........< E N T R Y ' S > .......................
        # ELEMENT GRAPHIQUE : <Entry> = [Libellé E01] : Entrée du pseudo
        # Création d'un widget Entry (champ de saisie)
        Nom = StringVar()
        EntreeNom = Entry(self, textvariable=Nom, bg='bisque', fg='red', font=("Arial", 20), )
        EntreeNom.focus_set()  # : nécessaire ?
        EntreeNom.place(x=10, y=100)

        # Message après vérifiaction de l'entrée du nom
        self.messageUtilisateurNom = StringVar()  # Variable de message d'erreur de saisie type stringvar() pour
        self.messageUtilisateurNom.set("...")  # maj Label pertinent.

        # ELEMENT GRAPHIQUE : <Label> = Message
        self.LblMessage = Label(self, textvariable=self.messageUtilisateurNom)
        self.LblMessage.place(x=100, y=150)

        # ...........< B U T T O N S >........................
        # Boutons "configuration commande" et "valider" en haut

        # Création d'un widget Button (bouton Valider)
        self.BoutonValidNom = Button(self, text='Valider', font=("Arial", 15), command=RecupNameDever)
        self.BoutonValidNom.place(x=10, y=150)

        print("ID =", self.IdJoueur)
        if self.IdJoueur != 0:
            # Déverouillage des boutons
            # ELEMENT GRAPHIQUE : <Button> = [Bouton B0?] : Configuration commande
            BoutConfCom = Button(self, text="Configuration Commandes", command=self.commandeOuvreF03)
            BoutConfCom.place(x=10, y=250)  # Bouton pour tester le verrouillage

        # ELEMENT GRAPHIQUE : <Button> = [Bouton B03] : ...??
        # ??? A FAIRE

        # ELEMENT GRAPHIQUE : <Button> = [Bouton B02] : jouer
            self.ouvreF02 = Button(self, text="jouer", command=self.commandeOuvreF02)
            self.ouvreF02.place(x=10, y=600)

        # ELEMENT GRAPHIQUE : <Button> = [Bouton B04] : ...??
        # ??? A FAIRE

        # ELEMENT GRAPHIQUE : <Button> = [Bouton B05] : ...??
        # ??? A FAIRE

        # ELEMENT GRAPHIQUE : <Button> = [Bouton B06] : ...??
        # ??? A FAIRE

        # ELEMENT GRAPHIQUE : <Button> = [A preciser] : Un bouton pour quitter l'application
        self.quitButton = Button(self, text="Quitter", command=self.destroy)
        self.quitButton.place(x=150, y=600)


        # ...........< L I S T B O X ' S > .......................
        # (Tkinter)LISTBOX : Liste des ID des joueurs de la base de données (déclaration & position)
        AffID = Listbox(self)
        AffID.place(x=400, y=26, width=100, height=500)

        # (Tkinter)LISTBOX : Liste des noms des joueurs de la base de données (déclaration & position)
        AffNom = Listbox(self)
        AffNom.place(x=500, y=26, width=100, height=500)

        # (Tkinter)LISTBOX : Liste des score des joueurs de la base de données (déclaration & position)
        AffScore = Listbox(self)
        AffScore.place(x=600, y=26, width=100, height=500)

        # (Tkinter)LISTBOX : Liste des Angles des joueurs de la base de données (déclaration & position)
        AffAngle = Listbox(self)
        AffAngle.place(x=700, y=26, width=100, height=500)

    # ==================================================
    # ELEMENTS GRAPHIQUES::::::::

    # COMMANDE : ouvre F02 (Jouer)
    def commandeOuvreF02(self):
        self.destroy()  # ferme F01
        # ouvre F02
        app = F02(self.IdJoueur)         # implémente l'objet app
        app.focus_force()   # Force le focus sur la fenetre
        app.mainloop()

    def commandeOuvreF03(self):
        self.destroy()  # ferme F01
        # ouvre F02
        app = F03(self.IdJoueur)         # implémente l'objet app
        app.mainloop()
