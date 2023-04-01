import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import numpy as np
import time

root = tk.Tk()
canvas = tk.Canvas(root, height = '500', width = '500')
canvas.pack()

#Create Title Lingo Balls
canvas.create_oval(30,10,100,80, outline = "medium blue", fill = "medium blue", width = 2)
canvas.create_oval(120,10,190,80, outline = "medium blue", fill = "medium blue", width = 2)
canvas.create_oval(210,10,280,80, outline = "medium blue", fill = "medium blue", width = 2)
canvas.create_oval(300,10,370,80, outline = "medium blue", fill = "medium blue", width = 2)
canvas.create_oval(390,10,460,80, outline = "medium blue", fill = "medium blue", width = 2)

#Print Letters Inside of Lingo Ball Circles
letterfont = tkFont.Font(size = 30)
l = canvas.create_text((65, 46), text= "L", font = letterfont, fill = "white")
i = canvas.create_text((155, 46), text= "I", font = letterfont, fill = "white")
n = canvas.create_text((245, 46), text= "N", font = letterfont, fill = "white")
g = canvas.create_text((335, 46), text= "G", font = letterfont, fill = "white")
o = canvas.create_text((425, 46), text= "O", font = letterfont, fill = "white")

#Create Homepage Game Board
canvas.create_rectangle(210,220,280,290, outline = "blue", fill = "blue", width = 200)
canvas.create_line(164,120,164,390, fill = "white")
canvas.create_line(218,120,218,390, fill = "white")
canvas.create_line(272,120,272,390, fill = "white")
canvas.create_line(326,120,326,390, fill = "white")
canvas.create_line(110,174,380,174, fill = "white")
canvas.create_line(110,228,380,228, fill = "white")
canvas.create_line(110,282,380,282, fill = "white")
canvas.create_line(110,336,380,336, fill = "white")

canvas.create_rectangle(110,120,164,174, outline = "white", fill = "red") #create red squares for correctly guessed letters
canvas.create_rectangle(110,174,164,228, outline = "white", fill = "red")
canvas.create_rectangle(110,228,164,282, outline = "white", fill = "red")
canvas.create_rectangle(110,282,164,336, outline = "white", fill = "red")
canvas.create_rectangle(110,336,164,390, outline = "white", fill = "red")
canvas.create_rectangle(272,174,326,228, outline = "white", fill = "red")
canvas.create_rectangle(164,228,218,282, outline = "white", fill = "red")
canvas.create_rectangle(164,336,218,390, outline = "white", fill = "red")
canvas.create_rectangle(218,336,272,390, outline = "white", fill = "red")
canvas.create_rectangle(272,336,326,390, outline = "white", fill = "red")
canvas.create_rectangle(326,336,380,390, outline = "white", fill = "red")
canvas.create_rectangle(164,282,218,336, outline = "white", fill = "yellow") #create yellow squares for guessed letters that are in word, but out of place
canvas.create_rectangle(218,282,272,336, outline = "white", fill = "yellow")
canvas.create_rectangle(272,282,326,336, outline = "white", fill = "yellow")


l = canvas.create_text((137, 147), text= "L", font = letterfont, fill = "white")
e = canvas.create_text((191, 147), text= "E", font = letterfont, fill = "white")
a = canvas.create_text((245, 147), text= "A", font = letterfont, fill = "white")
d = canvas.create_text((299, 147), text= "D", font = letterfont, fill = "white")
s = canvas.create_text((353, 147), text= "S", font = letterfont, fill = "white")


l = canvas.create_text((137, 201), text= "L", font = letterfont, fill = "white")
a = canvas.create_text((191, 201), text= "A", font = letterfont, fill = "white")
r = canvas.create_text((245, 201), text= "R", font = letterfont, fill = "white")
g = canvas.create_text((299, 201), text= "G", font = letterfont, fill = "white")
e = canvas.create_text((353, 201), text= "E", font = letterfont, fill = "white")

l = canvas.create_text((137, 255), text= "L", font = letterfont, fill = "white")
i = canvas.create_text((191, 255), text= "I", font = letterfont, fill = "white")
s = canvas.create_text((245, 255), text= "S", font = letterfont, fill = "white")
t = canvas.create_text((299, 255), text= "T", font = letterfont, fill = "white")
s = canvas.create_text((353, 255), text= "S", font = letterfont, fill = "white")

l = canvas.create_text((137, 309), text= "L", font = letterfont, fill = "white")
o = canvas.create_text((191, 309), text= "O", font = letterfont, fill = "white")
i = canvas.create_text((245, 309), text= "I", font = letterfont, fill = "white")
n = canvas.create_text((299, 309), text= "N", font = letterfont, fill = "white")
s = canvas.create_text((353, 309), text= "S", font = letterfont, fill = "white")

l = canvas.create_text((137, 363), text= "L", font = letterfont, fill = "white")
i = canvas.create_text((191, 363), text= "I", font = letterfont, fill = "white")
n = canvas.create_text((245, 363), text= "N", font = letterfont, fill = "white")
g = canvas.create_text((299, 363), text= "G", font = letterfont, fill = "white")
o = canvas.create_text((353, 363), text= "O", font = letterfont, fill = "white")

root.mainloop()