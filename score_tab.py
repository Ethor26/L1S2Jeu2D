#f = nom du fichier
from wF00 import *

def open_score_file():
    with open("scores.txt", 'r') as filin:
        score = filin.readlines()
        nb_line = len(score)
        tab = nb_line * [0]
        for i in range(len(tab)):
            tab[i] = nb_line * [0]
        for i in range(nb_line):
            score[i] = score[i].rstrip('\n')
            for j in range(nb_line):
                spell = score[j]
                spel = spell.split(";")
                tab[j]= spel
    return tab


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

def score_comparaison(score_player, best_score):
    if score_player < best_score:
        #nouveau label"vous ferez mieux la prochaine fois", ("Vous etes à" 'best_score-scoreplayer' du meilleur score)
    if score_player > best_score:
        #nouveau label "Bravo vous etes le nouveau meilleur gardien de la galaxie"

        # Il faut convertir les int en str avant d'écrire dans le fichier
        # f= nom du fichier


def ajout_nom_F000(name):
    with open("scores.txt", 'r') as file:
        score = file.readlines()
        nb_line = len(score)
        f = open("scores.txt", 'a')
        f.write('\n')
        nb_line = nb_line - 1
        id = str(nb_line)
        f.write(id)
        f.write(';')
        f.write(name)
        f.write(";")


def ajout_angle_F02(angle):
    with open("scores.txt", "a") as file:
        ang = str(angle)
        file.write(ang)
        file.write(";")


def ajout_score_F0(score):          #fenetre de jeu
    with open("scores.txt", "a") as f:
        sco = str(score)
        f.write(sco)

