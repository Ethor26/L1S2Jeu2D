from tkinter import *
import tkinter as tk
from random import *


def updatescore():
    global score
    chose = randint(1, 2)
    if chose == 2:
        score += 100
        score_variable.set(f'score: {score}')


self = Tk()
self.title("score update")
canvas = Canvas(self, width=150, height=150)
canvas.pack()
score = 0
b1 = Button(self, text="Update le score", command=updatescore).pack(side=RIGHT)
score_variable = tk.StringVar(self, f'score: {score}')
score_lbl = tk.Label(self, textvariable=score_variable).pack(side=LEFT)
self.mainloop()
