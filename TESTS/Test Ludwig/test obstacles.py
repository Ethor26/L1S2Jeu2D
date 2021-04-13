from tkinter import *
import math, random
from random import randrange as rr
from random import randint


######
# Définitions de fonctions

def action():
    "Animation"
    collide()
    move()
    fen.after(20, action)


def move():
    "Déplacement des balles"
    for i in range(len(balles)):
        balles[i]['x'] += balles[i]['dx']
        balles[i]['y'] += balles[i]['dy']
        can.coords(balls[i],
                   balles[i]['x'] - balles[i]['ray'],
                   balles[i]['y'] - balles[i]['ray'],
                   balles[i]['x'] + balles[i]['ray'],
                   balles[i]['y'] + balles[i]['ray'])


def collide():
    "Test de collision des balles"
    # Collision avec les parois
    for i in balles:
        if (i['x'] - i['ray']) <= 0 or (i['x'] + i['ray']) >= int(can['width']):
            i['dx'] = -i['dx']
        if (i['y'] - i['ray']) <= 0 or (i['y'] + i['ray']) >= int(can['height']):
            i['dy'] = -i['dy']
    # Collision entre les balles
    # ordre = 1/2, 1/3, 1/4, 2/3, 2/4, 3/4
    for i in range(len(balles)):
        j = i + 1
        while j < len(balles):
            # Test si (ray1+ray2)² > dist(x1-x2)² + dist(y1-y2)²
            # et interverti les dx et dy
            if (balles[i]['ray'] + balles[j]['ray']) ** 2 > \
                    ((balles[i]['x'] - balles[j]['x']) ** 2 +  # \
                     (balles[i]['y'] - balles[j]['y']) ** 2):
                balles[i]['dx'], balles[j]['dx'] = balles[j]['dx'], balles[i]['dx']
                balles[i]['dy'], balles[j]['dy'] = balles[j]['dy'], balles[i]['dy']
            j += 1


#######################
# Programme principal #
#######################

######
# Widget principal
fen = Tk()
fen.title("Obstacles")

######
# Variables
canW, canH = 640, 480
ray = 15

######
# Widget enfants
can = Canvas(fen, width=canW, height=canH, bg='white')
can.pack(side=TOP, padx=5, pady=5)

# position initiale aleatoire
listpos= [50,100,150,200,250,300,350,400]

# direction initiale aléatoire
vitesse = random.uniform(1.8, 2) * 5
angle = random.uniform(0, 2 * math.pi)
DX = vitesse * math.cos(angle)
DY = vitesse * math.sin(angle)

balle1 = {'x': listpos[randint(0,7)],
          'y': listpos[randint(0,5)],
          'ray': ray,
          'dx': random.uniform(1.8, 2) * 5 * math.cos(random.uniform(0, 2 * math.pi)),
          'dy': random.uniform(1.8, 2) * 5* math.sin(random.uniform(0, 2 * math.pi))}

balle2 = {'x': listpos[randint(0,7)],
          'y': listpos[randint(0,5)],
          'ray': ray,
          'dx': random.uniform(1.8, 2) * 5 * math.cos(random.uniform(0, 2 * math.pi)),
          'dy': random.uniform(1.8, 2) * 5* math.sin(random.uniform(0, 2 * math.pi))}

balle3 = {'x': listpos[randint(0,7)],
          'y': listpos[randint(0,5)],
          'ray': ray,
          'dx': random.uniform(1.8, 2) * 5 * math.cos(random.uniform(0, 2 * math.pi)),
          'dy': random.uniform(1.8, 2) * 5* math.sin(random.uniform(0, 2 * math.pi))}

balle4 = {'x': listpos[randint(0,7)],
          'y': listpos[randint(0,5)],
          'ray': ray,
          'dx': random.uniform(1.8, 2) * 5 * math.cos(random.uniform(0, 2 * math.pi)),
          'dy': random.uniform(1.8, 2) * 5* math.sin(random.uniform(0, 2 * math.pi))}

balles = (balle1, balle2, balle3, balle4)

ball1 = can.create_oval(balle1['x'] - balle1['ray'],
                        balle1['y'] - balle1['ray'],
                        balle1['x'] + balle1['ray'],
                        balle1['y'] + balle1['ray'],
                        fill='red')

ball2 = can.create_oval(balle2['x'] - balle2['ray'],
                        balle2['y'] - balle2['ray'],
                        balle2['x'] + balle2['ray'],
                        balle2['y'] + balle2['ray'],
                        fill='green')

ball3 = can.create_oval(balle3['x'] - balle3['ray'],
                        balle3['y'] - balle3['ray'],
                        balle3['x'] + balle3['ray'],
                        balle3['y'] + balle3['ray'],
                        fill='blue')

ball4 = can.create_oval(balle4['x'] - balle4['ray'],
                        balle4['y'] - balle4['ray'],
                        balle4['x'] + balle4['ray'],
                        balle4['y'] + balle4['ray'],
                        fill='yellow')

balls = (ball1, ball2, ball3, ball4)

Button(fen, text="Quitter", command=fen.quit).pack()

action()
fen.mainloop()
