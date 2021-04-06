from random import *
import tkinter as tk


WIDTH, HEIGHT = 500, 500


def create_pipes():
    pipes = []
    for x in range(0, WIDTH, 40):
        y1 = random.randrange(50, HEIGHT - 50)
        y0 = y1 + 50
        pipes.append(canvas.create_line(x, 0, x, y1))
        pipes.append(canvas.create_line(x, y0, x, HEIGHT))
    return pipes


#def move_pipes():
#    for pipe in pipes:
#        canvas.move(pipe, -2, 0)
#        x, y0, _, y1 = canvas.coords(pipe)
#        if x < 0:
#            canvas.coords(pipe, WIDTH+20, y0, WIDTH+20, y1)

#    if random.randrange(0, 20) == 10:
#        on_change()

#    root.after(40, move_pipes)


def on_change():
    global score
    chose = randint(1, 5)
    if chose == 2:
       score += 100
       score_variable.set(f'score: {score}')


root = tk.Tk()
tk.Button(root, text='start', command=on_change).pack()
score = 0
score_variable = tk.StringVar(root, f'score: {score}')
score_lbl = tk.Label(root, textvariable=score_variable)
score_lbl.pack()

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="cyan")
canvas.pack()

#pipes = create_pipes()

root.mainloop()