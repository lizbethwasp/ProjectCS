# Title of IA Solution
# Controller.py
# IDE - PyCharm Community Edition
# Python 3.6.0
# Platform - PC


import math
from Classes.Wire import Wire
from Classes.Pointer import Pointer


class Controller:

    pointers = []

    wires = []

    def __init__(self, GUI):
        self.GUI = GUI

    def place_wire(self, x, y, I, color):
        self.wires.append(Wire(x,y,I,self.GUI.canvas.create_oval(x+10,y+10,x-10,y-10,fill=color)))

    def draw_arrows(self, color):
        ppgv = self.GUI.canvas_width / len(self.GUI.grid['v']) # Pointers per grid vertical
        ppgh = self.GUI.canvas_height / len(self.GUI.grid['h']) # Pointers per grid horizontal

        if len(self.GUI.grid) == 0:
            raise Exception("Draw Grid first")

        for x in (range(1, len(self.GUI.grid['h']))):
            for y in (range(1, len(self.GUI.grid['v']))):
                self.pointers.append(Pointer(x * ppgh, y * ppgv, self.GUI.canvas, color=color, size=15))

    def mag_field_force(self, I, r):
        return I / (2 * math.pi * r)

    def calc_angle(self, p0, p1, p2):
        a = (p1[0] - p0[0]) ** 2 + (p1[1] - p0[1]) ** 2
        b = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        c = (p2[0] - p0[0]) ** 2 + (p2[1] - p0[1]) ** 2
        in_rad = math.acos((a + b - c) / math.sqrt(4 * a * b))
        if (p2[0] < p0[0] or p2[1] < p0[1]):
            return 360 - int(in_rad * 180 / math.pi)
        return int(in_rad * 180 / math.pi)

    def update(self):
        pass

    def calc_power(self, pointer, wire):
        distance = math.sqrt((pointer.x - wire.x) ** 2 + (pointer.y - wire.y) ** 2)
        return self.mag_field_force(wire.I,distance)

    def update_grid(self):
        for wire in self.wires:
            power_lambda = lambda x: self.calc_power(x,wire)
            angles_lambda = lambda x: self.calc_angle([wire.x,wire.y - math.sqrt((x.x - wire.x) ** 2 + (x.y - wire.y) ** 2)],[wire.x,wire.y],[x.x,x.y])
            powers = [*map(power_lambda,self.pointers)]
            angles = [*map(angles_lambda,self.pointers)]
            for ptr in range(len(self.pointers)):
                if powers[ptr] > 0.001:
                    self.pointers[ptr].rotate_pointer(angles[ptr]+90)
                elif powers[ptr] < -0.001:
                    self.pointers[ptr].rotate_pointer(angles[ptr]+270)