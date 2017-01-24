from tkinter import *

root = Tk()

frame = Frame(root, width=500, height=500)

canvas = Canvas(frame, width=500, height=500)

def callback(event):
    print ("clicked at", event.x, event.y)

canvas.create_oval(100,100,120,120,fill="black")
canvas.pack()

frame.pack()

root.mainloop()