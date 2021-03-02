from tkinter import *


def Clavier(event):
    """ Gestion de l'événement Appui sur une touche du clavier """
    global PosX, PosY
    touche = event.keysym
    print(touche)
    # déplacement vers le haut
    if touche == 'a':
        PosY -= 20
    # déplacement vers le bas
    if touche == 'q':
        PosY += 20
    # déplacement vers la droite
    if touche == 'm':
        PosX += 20
    # déplacement vers la gauche
    if touche == 'l':
        PosX -= 20
    # on dessine le pion à sa nouvelle position
    Canevas.coords(Pion, PosX - 10, PosY - 10, PosX + 10, PosY + 10)


# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title('Pion')

# position initiale du pion
PosX = 230
PosY = 150

# Création d'un widget Canvas (zone graphique)
Largeur = 480
Hauteur = 320
Canevas = Canvas(Mafenetre, width=Largeur, height=Hauteur, bg='white')

Pion = Canevas.create_oval(PosX - 10, PosY - 10, PosX + 10, PosY + 10, width=2, outline='black', fill='red')

Canevas.focus_set()
Canevas.bind('<Key>', Clavier)
Canevas.pack(padx=5, pady=5)

# Création d'un widget Button (bouton Quitter)
Button(Mafenetre, text='Quitter', command=Mafenetre.destroy).pack(side=LEFT, padx=5, pady=5)

Mafenetre.mainloop()

# script animation_balle.py
# (C) Fabrice Sincère

from tkinter import *
import math, random

LARGEUR = 480
HAUTEUR = 320
RAYON = 15  # rayon de la balle

# position initiale au milieu
X = LARGEUR / 2
Y = HAUTEUR / 2

# direction initiale aléatoire
vitesse = random.uniform(1.8, 2) * 5
angle = random.uniform(0, 2 * math.pi)
DX = vitesse * math.cos(angle)
DY = vitesse * math.sin(angle)


def deplacement():
    """ Déplacement de la balle """
    global X, Y, DX, DY, RAYON, LARGEUR, HAUTEUR

    # rebond à droite
    if X + RAYON + DX > LARGEUR:
        X = 2 * (LARGEUR - RAYON) - X
        DX = -DX

    # rebond à gauche
    if X - RAYON + DX < 0:
        X = 2 * RAYON - X
        DX = -DX

    # rebond en bas
    if Y + RAYON + DY > HAUTEUR:
        Y = 2 * (HAUTEUR - RAYON) - Y
        DY = -DY

    # rebond en haut
    if Y - RAYON + DY < 0:
        Y = 2 * RAYON - Y
        DY = -DY

    X = X + DX
    Y = Y + DY

    # affichage
    Canevas.coords(Balle, X - RAYON, Y - RAYON, X + RAYON, Y + RAYON)

    # mise à jour toutes les 50 ms
    Mafenetre.after(50, deplacement)


# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title("Animation Balle")

# Création d'un widget Canvas
Canevas = Canvas(Mafenetre, height=HAUTEUR, width=LARGEUR, bg='white')
Canevas.pack(padx=5, pady=5)

# Création d'un objet graphique
Balle = Canevas.create_oval(X - RAYON, Y - RAYON, X + RAYON, Y + RAYON, width=1, fill='green')

deplacement()
Mafenetre.mainloop()