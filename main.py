# ======================================================
# PROJET TRANSVERSE 1 L1 : Jeu 2D Python
# Auteurs : Equipe ShirosakiBest = Ethan SUISSA, Lilandra ALBERT-LAVAULT, Pierre REY, Jean-Alexis TADDEI, Ludwig
# NEUBERTH- EFREI -L1 BN
# Date : 4 mai 2021 (?)
# Fichier principal
# ======================================================
import pygame

from wF00 import F00
import os

# ETAPE 1 : Récupération du Chemin d'accès du fichier la base de données
cheminAcces = os.getcwd() + "/Scores.txt"  # os.getcwd() donne le chemin d'accès jusqu'au repertoire du projet
print("main : cheminAcces=" + cheminAcces)

pygame.init()
# pygame.mixer.pre_init()
pygame.mixer.init()



# ETAPE 2 : lancement de la fenetre d'ouverture
def main():
    print("OUVERTURE DE L'APPLICATION (Fenetre F00)")  # pour controle en console
    # pygame.mixer.music.load("audio.mp3")
    # pygame.mixer.music.play(-1)
    app = F00("debut")
    app.mainloop()  # Ouverture de la fenêtre d'ouverture F00.


# execution par Run pour exe
if __name__ == '__main__':
    main()
