#f = nom du fichier
def open_score_file(f):
    with open(f, 'r') as filin:
        score = filin.readlines()
        nb_line = len(score)
        for i in range(nb_line):
            score[i] = score[i].rstrip('\n')
    return score


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

def score_comparaison(score_tab, best_score):
    if score_player < best_score:
        #nouveau label"vous ferez mieux la prochaine fois", ("Vous etes à" 'best_score-scoreplayer' du meilleur score)
    if score_player > best_score:
        #nouveau label "Bravo vous etes le nouveau meilleur gardien de la galaxie"

        # Il faut convertir les int en str avant d'écrire dans le fichier
        # f= nom du fichier