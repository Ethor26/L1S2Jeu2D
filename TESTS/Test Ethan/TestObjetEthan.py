# Version objet
from Tools import *

class ProgCommandParam():
    # Constructeur de l'objet F01 : ne pas supprimer !!!
    def __init__(self, event2, angle, Canvas, Pion):
        """ Gestion de l'événement Appui sur une touche du clavier """
        global PosX, PosY
        touche = event2.keysym
        print(touche)
        VarX = 4
        # déplacement programmable
        if touche == 'p':
            for i in range(5): # Pour déplacement progressif
                PosY += int(CalcProg(angle, VarX))
                PosX += 4

        # on dessine le pion à sa nouvelle position
        Canvas.coords(Pion, PosX - 10, PosY - 10, PosX + 10, PosY + 10)



