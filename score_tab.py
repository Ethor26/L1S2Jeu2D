#f = nom du fichier
def open_score_file(f):
    score_tab = []
    with open(f, 'r') as filin:
        score = filin.readlines()
        while score != ' ':
            print(score)
        for i in score:
            i.split()
    for ligne in f:
        score_tab[i]
        temp_tab =  ligne.split()
        for i in score_tab:
            score_tab[i] == temp_tab

    return score_tab

def ajout_score(f, id, user, angle, score):
    with open(f, 'a') as file:
        file.write('\n')
        file.write(id)
        file.write(' ')
        file.write(user)
        file.write(' ')
        file.write(angle)
        file.write(' ')
        file.write(score)
    return f


def score_comparaison(score_tab, best_score):
    if score_tab[4] < best_score:
        #fonction ouverture fenetre "vous ferez mieux la prochaine fois"
    if score_tab[4] > best_score:
        #fonction ouverture fenetre "Bravo vous etes le nouveau meilleur gardien de la galaxie"

        # Il faut convertir les int en str avant d'écrire dans le fichier
        # f= nom du fichier