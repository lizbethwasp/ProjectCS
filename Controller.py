# Title of IA Solution
#  ______
# IDE - PyCharm Community Edition
# Python 3.6
# Platform - Windows, Mac Linux


import math
from Classes.Wire import Wire
from  Classes.Pointer import Pointer


class Controller:

    pointers = []

    wires = []

    def __init__(self, GUI):
        self.GUI = GUI

    def place_wire(self, x, y, I, color):
        self.wires.append(Wire(x,y,I,self.GUI.canvas.create_oval(x+10,y+10,x-10,y-10,fill=color)))

    def draw_arrows(self, color):
        ppgv = self.GUI.canvas_width // len(self.GUI.grid['v']) # Pointers per grid vertical
        ppgh = self.GUI.canvas_height // len(self.GUI.grid['h']) # Pointers per grid horizontal

        print (ppgv, ppgh)

        if (len(self.GUI.grid) == 0):
            raise Exception("Draw Grid first");

        for x in (range(1, len(self.GUI.grid['h']))):
            for y in (range(1, len(self.GUI.grid['v']))):
                self.pointers.append(Pointer(x * ppgh,y * ppgh, self.GUI.canvas, color=color))

    def mag_field_force(self, I, r):
        return I / (2 * math.pi * r)

    def update(self):
        self.poniters[0].rotate_pointer()

