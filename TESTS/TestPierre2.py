from tkinter import *

fenetre= Tk()
photo = PhotoImage(file="background.png")
canvas = Canvas(fenetre, width=1200, height=700)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()
lbl = canvas.create_text(600, 350, text="Il y a bien longtemps, une galaxie lointaine était dirigée par un Conseil\n"
                       "de sages qui s’efforçaient à ce que tous le monde vive une vie paisible.\n"
                       "Malheureusement, ils virent bientôt apparaître une armée menée par un\n"
                       "empereur infecté par un virus nommé Galacticov. Ce virus avait paralysé\n"
                       "toutes les zones du cerveau de l’empereur qui lui permettait d’éprouver\n"
                       "des émotions négatives et stimulé les connexions dans celles créant des\n"
                       "émotions négatives. Un empereur juste et intègre devint alors cruel et\n "
                       "implacable.Ce virus étant contrôlé à distance par un conseiller avide\n "
                       "de pouvoir dans une centrale, le Conseil vous recruta avec d’autres héros\n"
                       "pour atteindre et détruire cette centrale, en évitant les tirs des vaisseaux\n"
                       "délégué par l’empereur. Vous, <Nom à définir>, devrez donc passer à travers \n"
                       "cette armée, mais avec l’interdiction du Conseil de détruire les autres vaisseaux.\n"
                       "En effet, ils sont contrôlés par des pilotes innocents mais manipulés. Ils ignorent\n"
                       "vos objectifs et s’imaginent que vous venez détruire leur empire. Une quête ardue \n"
                       "commence pour vous…\n", font='Arial 18 bold', fill='black')
canvas.pack()
b1 = Button(fenetre, text="Close", command=fenetre.quit).pack(side=RIGHT)
b2 = Button(fenetre, text="Play", command=fenetre).pack(side=LEFT)
label = Label(fenetre, text="Saisir votre pseudo", bg="green").pack(side=BOTTOM)
value = StringVar()
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=label, width=30)
entree.pack()
fenetre.mainloop()