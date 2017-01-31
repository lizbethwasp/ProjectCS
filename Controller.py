# Title of IA Solution
#  ______
# IDE - PyCharm Community Edition
# Python 3.6
# Platform - Windows, Mac, Linux


import math
from Classes.Wire import Wire
from Classes.Pointer import Pointer


class Controller:

    pointers = []

    wires = []

    def __init__(self, GUI):
        self.GUI = GUI
        self.GUI.canvas.bind("<Button-1>", lambda event: self.detect_wire(event))
        self.GUI.canvas.bind("<B1-Motion>", lambda event: self.transit_wire(event))
        self.GUI.canvas.bind("<ButtonRelease-1>", lambda event: self.move_wire(event))
        self.GUI.canvas.bind("<Button-2>", lambda event: self.place_wire(event.x,event.y,1,color="black",size=10))

    def detect_wire(self, event):
        print(event.widget.find_closest(event.x, event.y))
        for wire in self.wires:
            print(wire.GUI_sign)
            if wire.GUI_sign == event.widget.find_closest(event.x, event.y)[0]:
                self.active_wire = wire

    def transit_wire(self, event):
        if self.active_wire:
            self.active_wire.x = event.x
            self.active_wire.y = event.y
            self.active_wire.redraw()

    def move_wire(self, event):
        self.transit_wire(event)
        self.update_grid()
        self.active_wire = 0

    def place_wire(self, x, y, I, color, size):
        self.wires.append(Wire(x, y, I, color, size, self.GUI.canvas))
        self.update_grid()

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
        if p2[0] < p0[0] or p2[1] < p0[1]:
            return 360 - int(in_rad * 180 / math.pi)
        return int(in_rad * 180 / math.pi)

    def update(self):
        pass

    def calc_power(self, pointer, wire):
        distance = math.sqrt((pointer.x - wire.x) ** 2 + (pointer.y - wire.y) ** 2)
        return self.mag_field_force(wire.I, distance)

    def update_grid(self):
        for ptr in range(len(self.pointers)):
            self.pointers[ptr].rotate_to_0()
        for wire in self.wires:
            power_lambda = lambda x: self.calc_power(x,wire)
            angles_lambda = lambda x: self.calc_angle([wire.x,wire.y - math.sqrt((x.x - wire.x) ** 2 + (x.y - wire.y) ** 2)],[wire.x,wire.y],[x.x,x.y])
            powers = [*map(power_lambda,self.pointers)]
            angles = [*map(angles_lambda,self.pointers)]
            for ptr in range(len(self.pointers)):
                if powers[ptr] > 0.001:
                    if self.pointers[ptr].direction == 0:
                       self.pointers[ptr].rotate_pointer(90)
                    self.pointers[ptr].rotate_pointer(angles[ptr])
                elif powers[ptr] < -0.001:
                    if self.pointers[ptr].direction == 0:
                       self.pointers[ptr].rotate_pointer(270)
                    self.pointers[ptr].rotate_pointer(angles[ptr])
        for wire in self.wires:
            wire.redraw()