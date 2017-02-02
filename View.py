# Title of IA Solution
# View.py
# IDE - PyCharm Community Edition
# Python 3.6.0
# Platform - PC


import tkinter


class GUI:


    def __init__(self, canvas_height, canvas_width):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.root = tkinter.PanedWindow(orient=tkinter.HORIZONTAL)
        self.root.pack(fill=tkinter.BOTH, expand=1)
        self.canvas = tkinter.Canvas(self.root, width=canvas_width, height=canvas_height)
        self.root.add(self.canvas)
        self.scale = tkinter.Scale(self.root, from_=-2, to=2, resolution=0.01, orient=tkinter.HORIZONTAL)
        self.root.add(self.scale)
        self.delButton = tkinter.Button(self.root,text="Delete")
        self.root.add(self.delButton)

    def show(self):
        self.canvas.pack()
        self.scale.pack()
        self.delButton.pack()
        tkinter.mainloop()
