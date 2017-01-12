import math
from Classes.Wire import Wire


class Controller:

    pointers = []

    wires = []

    def __init__(self, GUI):
        self.GUI = GUI

    def place_wire(self, x, y, I, color):
        self.wires.append(Wire(x,y,I,self.GUI.canvas.create_oval(x+10,y+10,x-10,y-10,fill=color)))

    def mag_field_force(self, I, r):
        return I / (2 * math.pi * r)

    def update(self):
        self.GUI.pointers = [*map()]

