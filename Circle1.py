import tkinter
import random
import time

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=400, height=400)
canvas.pack()

colors = ('aquamarine1', 'CornflowerBlue', 'dark orchid', 'DodgerBlue4', 'GreenYellow', 'grey', 'LightSalmon3')

radius = []
for rad in range(150, 181, 5):
    radius.append(rad)

while True:
    center = random.randint(0, 400)
    for ind, color in enumerate(colors):
        canvas.create_oval(center - radius[ind], center - radius[ind], center + radius[ind], center + radius[ind],
                           outline=color)
        canvas.update()
        time.sleep(0.05)

window.mainloop()