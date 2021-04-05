## ======================================================
# PROJET TRANSVERSE 1 L1 : Jeu 2D Python
# Auteurs : Equipe ShirosakiBest = Ethan SUISSA, Lilandra ALBERT-LAVAULT, Pierre REY, Jean-Alexis TADDEI, Ludwig
# NEUBERTH- EFREI -L1 BN
# Date : 4 mai 2021 (?)
# Fichier outils
# ======================================================
# from math import *


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
# -----------------------------------------------------------------------------------
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
# FONCTION OUTIL : Ecriture dans la base de donnée. Auteur : Jean-Alexis TADDEI- en cours
def ajout_score(f, id, user, angle, score):
    with open(f, 'a') as file:
        file.write('\n')
        file.write(id)
        file.write(';')
        file.write(user)
        file.write(';')
        file.write(angle)
        file.write(';')
        file.write(score)


def ajout_nom_F000(name):
    with open("scores.txt", 'r') as file:
        score = file.readlines()
        print("fichier =", score)
        nb_line = len(score)
        f = open("scores.txt", 'a')
        f.write('\n')
        nb_line = nb_line - 1
        id = str(nb_line)
        f.write(id + ';' + name + ";")
        # Possibilité de faire plusieurs "file.write"  à la suite ou concaténer les chaines


def ajout_angle_F02(angle):
    with open("scores.txt", "a") as file:
        ang = str(angle)
        file.write(ang + ";")


def ajout_score_F0(score):  # fenetre de jeu
    with open("scores.txt", "a") as f:
        sco = str(score)
        f.write(sco)


# =============================================================================
# FONCTION OUTIL : Lecture de la base de donnée. Auteur : Jean-Alexis TADDEI- en cours
def open_score_file2():
    with open("scores.txt", 'r') as filin:
        score = filin.readlines()
        nb_line = len(score)
        tab = []
        for i in range(nb_line):
            score[i] = score[i].rstrip('\n')
            spell = score[i]
            spel = spell.split(";")
            tab.append(spel)
        filin.close()
    print(tab)
    return tab, nb_line


# print(open_score_file2())

# =============================================================================
# FONCTION OUTIL : Comparaison Score. Auteur : Jean-Alexis TADDEI- en cours
def score_comparaison2(Score, IdJoueur):
    # on regarde dans le txt quel est le meilleur score on doit utiliser la fonction open_score_file afin d'utiliser
    # le tableau avec le score
    tab, nb_ligne = open_score_file2()
    best_score = int(tab[IdJoueur + 2][3])
    if Score >= best_score:
        best_score = Score
    return best_score


# Score = 1
# print(score_comparaison2(Score))


# =============================================================================
# FONCTION OUTIL : Modifier Ligne Auteur : Ethan SUISSA- en cours
def modifierLigne(cheminAccesFichier, pId, pNom, pAngle, pScore):
    global line
    IdRecherche = pId + ";"

    ligneAecrire = pId + ";" + pNom + ";" + pAngle + ";" + pScore
    LigneTrouve = False
    fichier = open(cheminAccesFichier, "a")  # ouverture du fichier à modifier
    for line in fichier:  # boucle sur les lignes du fichier original
        if IdRecherche in line:
            print("modifierLigne : Id trouvé = ", pId)
            print("Line = ", line)
            line = ligneAecrire
            LigneTrouve = True

    if LigneTrouve == True:
        fichier.write(line)
    fichier.close()


# =============================================================================
# FONCTION OUTIL : Modifie précisément un élément de la ligne de la base de donnée. Auteur : Ethan SUISSA- terminé
import fileinput


def ModifPrecisFichier(NumLigne, NumElt, Modif):
    tab, nbLignes = open_score_file2() # Lecture de la base de donnée

    # Enregistrement de la ligne à modifier
    OldLigne = ""
    for i in range(3):
        OldLigne += tab[NumLigne][i] + ";" # Addition de chaque élément du tableau pour reformer la ligne
    OldLigne += tab[NumLigne][3]
    print("Ancienne ligne", OldLigne) # Pour control

    # Enregistrement de la ligne à appliquer à la place d'OldLine
    tab[NumLigne][NumElt] = str(Modif) # Modification de l'élément demandé
    NewLigne = ""
    for i in range(3):
        NewLigne += tab[NumLigne][i] + ";" # Même addition que précedemment
    NewLigne += tab[NumLigne][3]  # Ligne à appliquer à la place de l'ancienne
    print("Nouvelle ligne", NewLigne)

    with fileinput.input("scores.txt", inplace=True) as f: # Configure le fichier pour cette modification (trouvé sur
        # internet).
        for line in f:
            new_line = line.replace(OldLigne, NewLigne)  # Modification de la ligne en remplacant l'ancienne par la
            # nouvelle
            print(new_line, end='') # n'affiche rien mais enlève les blancs intermédiaires
    # Test : ModifPrecisFichier(3, 2, 1)
