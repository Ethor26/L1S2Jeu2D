import math

from tkinter import *
from math import *

Largeur = 480  # Largeur Ecran Jeu
Hauteur = 320  # Hauteur Ecran Jeu
Rayon = 10  # rayon de l'objet
ValeurPas = 4  # Nombre de pas de déplacement


AngleEnDegree = 200

# position initiale du pion
PosX = 230
PosY = 150


# Version fonction
def CommandeClavier(event):
    """ Gestion de l'événement Appui sur une touche du clavier """
    touche = event.keysym  # Un événement (event) est la survenue d’une action (clavier, souris) dont votre application a besoin d’être informée

    # Si touche ? => deplt a droite
    # A CODER

    # Si touche ? => deplt a Gauche
    # A CODER

    # Si touche ? => deplt a bas
    # A CODER

    # Si touche ? => deplt a Haut
    # A CODER

    if touche == 'p':
        Mafenetre.after(100, deplacement_P)   # Lance la fonction toute les 100 ms

# =============================================================================
# Fonction de déplacement de la touche P
def deplacement_P():
    global PosX, PosY
    for i in range(3):
        PosX, PosY = ValeurPosXY(PosX, PosY, ValeurPas + i)

    print("posY = ", PosY)  # pour controle
    print("posX = ", PosX)  # pour controle
    print("Pion = ", Pion)  # pour controle
    Canevas.coords(Pion, PosX - 10, PosY - 10, PosX + 10, PosY + 10)


# FONCTION OUTIL: Calcul de la commande programmable. Auteur : Ethan SUISSA - En cours
def ValeurAngleParametreEnRadian():
    # codage à faire : Récupérer angle dans score.txt
    print("Angle en degree = ", AngleEnDegree)
    angleRadian = math.radians(AngleEnDegree)  # valeur par defaut
    return angleRadian


# Utilise l'équation de mouvement pour calculer la postion finale en fonction de l'angle
def CalcProg(AngleDeduitDegree, posXFinal, valH):
    v0 = 5  # Choix de vitesse à 5
    g = 9.81  # Constante de gravitation
    Angle_Deduit_Radian = math.radians(AngleDeduitDegree)  # convertion en Radian de l'angle deduit
    Eqmouv = (-1 / 2) * ((g * posXFinal ** 2) / (v0 * cos(Angle_Deduit_Radian)) ** 2) + tan(
        Angle_Deduit_Radian) * posXFinal + valH
    AdaptEqMouv = int(Eqmouv)
    return AdaptEqMouv


def ValeurPosXY(valX_Initial, valY_Initial, NbPas):
    print("ValPosXY :  valXInitial =", valX_Initial)
    print("ValPosXY :  valYInitial =", valY_Initial)

    # Bloc 1
    if 0 < AngleEnDegree < 89:
        print("ValPosXY :  Bloc 1 ")  # pour controle
        valX_Final = valX_Initial + NbPas
        valY_Final = CalcProg(AngleEnDegree, NbPas, valY_Initial)

    # Bloc 2
    if 90 < AngleEnDegree < 179:
        print("ValPosX :  Bloc 2 : Position x")  # pour controle
        Angle_Deduit_Degree = AngleEnDegree - 90
        valY_Final = valY_Initial + NbPas
        valX_Final = CalcProg(Angle_Deduit_Degree, NbPas, valX_Initial)

    # Bloc 3
    if 180 < AngleEnDegree < 269:
        print("ValPosX :  Bloc 3 : Position x")  # pour controle
        Angle_Deduit_Degree = AngleEnDegree - 180
        valX_Final = valX_Initial - NbPas
        valY_Final = - CalcProg(Angle_Deduit_Degree, NbPas, valY_Initial)

    # Bloc 4
    if 270 < AngleEnDegree < 360:
        print("ValPosX :  Bloc 4 : Position X ")  # pour controle
        Angle_Deduit_Degree = AngleEnDegree - 270
        valY_Final = int(valY_Initial - NbPas)
        valX_Final = CalcProg(Angle_Deduit_Degree, NbPas, valX_Initial)

    print("ValPosXY : ValXFinal avant correction = ", valX_Final)
    print("ValPosXY : ValYFinal avant correction = ", valY_Final)

    # Corrige la position X si on sort du cadre
    if valX_Final > Largeur - Rayon:
        print("ValPosXY (posX):  Sortie du cadre à droite => Rebond ")
        valX_Final = valX_Initial - Rayon

    if valX_Final < Rayon:
        print("ValPosXY (posX):  Sortie du cadre à gauche => Rebond ")
        valX_Final = valX_Initial + Rayon

    # Rebond en bas
    if valY_Final < Rayon:
        print("ValPosXY (posY):  Sortie en bas ==> Rebond")
        valY_Final = valY_Initial + Rayon
    # Rebond en haut
    if valY_Final > Hauteur - Rayon:
        print("ValPosXY (posY):  Sortie en haut ==> Rebond")
        valY_Final = valY_Initial - Rayon

    return valX_Final, valY_Final


# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title('Pion')

# Création d'un widget Canvas (zone graphique)
Canevas = Canvas(Mafenetre, width=Largeur, height=Hauteur, bg='white')
Pion = Canevas.create_oval(PosX - 10, PosY - 10, PosX + 10, PosY + 10, width=2, outline='black', fill='red')
Canevas.focus_set()

Canevas.bind('<Key>', CommandeClavier)
Canevas.pack(padx=5, pady=5)

# Création d'un widget Button (bouton Quitter)
Button(Mafenetre, text='Quitter', command=Mafenetre.destroy).pack(side=LEFT, padx=5, pady=5)

Mafenetre.mainloop()
