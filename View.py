# Title of IA Solution
#  ______
# IDE - PyCharm Community Edition
# Python 3.6
# Platform - Windows, Mac Linux


import tkinter


class GUI:

    grid = {}

    def __init__(self, canvas_height, canvas_width):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.root = tkinter.PanedWindow(orient=tkinter.HORIZONTAL)
        self.root.pack(fill=tkinter.BOTH, expand=1)
        self.canvas = tkinter.Canvas(self.root, width=canvas_width, height=canvas_height)
        self.root.add(self.canvas)
        self.active_wire_label = tkinter.Label(self.root)
        self.root.add(self.active_wire_label)
        self.scale = tkinter.Scale(self.root, from_=-2, to=2, resolution=0.01, orient=tkinter.HORIZONTAL)
        self.root.add(self.scale)
        self.delButton = tkinter.Button(self.root,text="Delete")
        self.root.add(self.delButton)

    def draw_grid(self, line_number, color):

        if len(self.grid) != 0:
            raise Exception("Must be only one Grid")

        g = {}  # Grid
        v = []  # Verticals
        h = []  # Horizontals

        for x in range(line_number):
            v.append(self.canvas.create_line(0, (self.canvas_width / line_number) * x,
                                             self.canvas_width,
                                             (self.canvas_width / line_number) * x, fill=color))
            h.append(self.canvas.create_line((self.canvas_width / line_number) * x, 0,
                                             (self.canvas_width / line_number) * x, self.canvas_width, fill=color))

        g["h"] = h
        g["v"] = v
        self.grid = g

    def show(self):
        self.active_wire_label.pack()
        self.canvas.pack()
        self.scale.pack()
        self.delButton.pack()
        tkinter.mainloop()
