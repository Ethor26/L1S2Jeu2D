## ======================================================
# PROJET TRANSVERSE 1 L1 : Jeu 2D Python
# Auteurs : Equipe ShirosakiBest = Ethan SUISSA, Lilandra ALBERT-LAVAULT, Pierre REY, Jean-Alexis TADDEI, Ludwig
# NEUBERTH- EFREI -L1 BN
# Date : 4 mai 2021 (?)
# Fichier outils
# ======================================================
from math import *

# ========================================================================================
# FONCTION OUTIL: fonction COMPLEMENTAIRE aux précédentes qui retourner la clé d'un dictionnaire avec en entrée
# celui-ci et une de ses valeurs.  Auteur : Ethan SUISSA - Terminé
def find_key(Dict, Val):
    for key, val in Dict.items():
        if Val == val:
            return key



# ===================================================================================
# FONCTION OUTIL: Renvoie la ligne choisie du fichier indiqué dans une chaine de caractère (équivalent de read_file_line
# avec le chemin d'accès en entrée) Auteur : Ethan SUISSA - Terminé
# Sortie : Chaine de caractère qui contient la ligne récupérée
#-----------------------------------------------------------------------------------
def lireLaLignechoisie(chemin_acces, noLine):  # Entrée :  Chemin_acces = chemin d'acces du fichier, # noline = Numero
    # de la ligne
    line = ""
    # Vérifie si le chemin existe ou non
    import os.path
    if os.path.isfile(chemin_acces):
        print("Chemin ", chemin_acces, " existe")  # pour controle

        # Recupere le contenu de la ligne dans le fichier
        file = open(chemin_acces, 'r')
        for i in range(noLine):
            line = file.readline()
        file.close()
    else:
        print("Chemin ", chemin_acces, " n'existe pas")  # pour controle
    return line

# =============================================================================
# FONCTION OUTIL : Fermer un fichier

def closeFile(f):
    f.close()
# =============================================================================
# FONCTION OUTIL: Permet le déplacement par commande programmable. Auteur : Ethan SUISSA - En cours

# =============================================================================
# FONCTION OUTIL: Calcul de la commande programmable. Auteur : Ethan SUISSA - En Cours
def CalcProg(angle, VarX):
    v0 = 10**2
    g = 9.81
    Eqmouv = (-1/2) * ((g*VarX**2)/(v0 * cos(angle))**2) + tan(angle)*VarX
    return(Eqmouv)





