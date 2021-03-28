# f = nom du fichier

def open_score_file():
    with open("scores.txt", 'r') as filin:
        score = filin.readlines()
        print(score)
        nb_line = len(score)
        tab = nb_line * [0]
        for i in range(len(tab)):
            tab[i] = nb_line * [0]
        for i in range(nb_line):
            score[i] = score[i].rstrip('\n')
            for j in range(nb_line):
                spell = score[j]
                spel = spell.split(";")
                tab[j] = spel
    return tab
print(open_score_file())



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
        f.write(id)
        f.write(';')
        f.write(name)
        f.write(";")


def ajout_angle_F02(angle):
    with open("scores.txt", "a") as file:
        ang = str(angle)
        file.write(ang)
        file.write(";")


def ajout_score_F0(score):  # fenetre de jeu
    with open("scores.txt", "a") as f:
        sco = str(score)
        f.write(sco)


def score_comparaison1():
    # on regarde dans le txt quel est le meilleur score on doit utiliser la fonction open_score_file afin d'utiliser
    # le tableau avec le score
    best_score = 0
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
                tab[j] = spel

    print(tab)
    for i in range(1, len(tab) - 1):
        temp_score = tab[i][3]
        temp_score2 = int(temp_score)
        if best_score < temp_score2:
            best_score = temp_score2
    temp_perso_score = tab[nb_line - 1][3]
    temp_pers = int(temp_perso_score)
    if temp_pers > best_score:
        best_score = temp_pers
    return best_score
print(score_comparaison1())

# Versions Ethan

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
    print(tab)
    return tab, nb_line
# print(open_score_file2())

def score_comparaison2():
    # on regarde dans le txt quel est le meilleur score on doit utiliser la fonction open_score_file afin d'utiliser
    # le tableau avec le score
    best_score = 0
    tab, nb_ligne = open_score_file2()

    for i in range(1, len(tab) - 1):
        temp_score = tab[i][3]
        temp_score2 = int(temp_score)
        if best_score < temp_score2:
            best_score = temp_score2
    temp_perso_score = tab[nb_ligne - 1][3]
    temp_pers = int(temp_perso_score)
    if temp_pers > best_score:
        best_score = temp_pers
    return best_score
print(score_comparaison2())