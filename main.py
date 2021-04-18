# ======================================================
# PROJET TRANSVERSE 1 L1 : Jeu 2D Python
# Auteurs : Equipe ShiridzzddzqdsqdqzdqsdqzdpppposakiBest = Ethan SUISSA, Lilandra ALBERT-LAVAULT, Pierre REY, Jean-Alexis TADDEI, Ludwig
# NEUBERTH- EFREI -L1 BN
# Date : 4 mai 2021 (?)
# Fichier principal
# ======================================================
from wF00 import F00
import os

# ETAPE 1 : Récupération du Chemin d'accès du fichier la base de données
cheminAcces = os.getcwd() + "/Scores.txt"  # os.getcwd() donne le chemin d'accès jusqu'au repertoire du projet
print("main : cheminAcces=" + cheminAcces)


# ETAPE 2 : lancement de la fenetre d'ouverture
def main():
    print("OUVERTURE DE L'APPLICATION (Fenetre F00)")  # pour controle en console
    app = F00("debut")
    app.mainloop()


# execution par Run pour exe
if __name__ == '__main__':
    main()
