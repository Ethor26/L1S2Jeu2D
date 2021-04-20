from tkinter import *
import time


def F02():
    self = Tk()
    self.title("F02")
    canvas = Canvas(self, width=500, height=300)
    canvas.configure(background='black')
    canvas.pack()
    canvas.create_text(250, 150, text="Okok mec", font='25', fill='white')
    self.mainloop()


def F04(score, t4):
    personal_best = 150
    self = Tk()
    self.title("F04")
    canvas = Canvas(self, width=500, height=300)
    canvas.configure(background='black')
    canvas.pack()
    if (score>personal_best):
        Bravo = canvas.create_text(250, 150, text="Bravo, vous avez battu votre record !\nVotre score est : {}\nVotre ancien meilleur score était : {}\nVous avez tenu : {} secondes".format(score, personal_best,t4), font='Gabriola 17', fill='white')
    else:
        Dommage = canvas.create_text(250, 150, text="Dommage, vous ferez mieux la prochaine fois !\n Votre score est : {}\nVotre meilleur score est : {}\nVous avez tenu : {} secondes".format(score, personal_best,t4), font='Gabriola 17', fill='white')
    b1 = Button(self, text="Quitter", command=self.destroy).place(x=10, y=270)
    b2 = Button(self, text="Rejouer", command=self).place(x=60, y=270)
    self.mainloop()


def UpdateScore():
    score = 0
    t1 = time.time()
    F02()
    t2 = time.time()
    t3 = t2-t1
    t4 = t3
    while t3 > 0.2:
        score += 5
        t3 -= 0.2
    F04(score, t4)


UpdateScore()
