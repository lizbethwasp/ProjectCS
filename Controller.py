import math


class Controller:

    pointers = []

    wires = []

    def __init__(self, GUI):
        self.GUI = GUI

    def mag_field_force(self, I, r):
        return I / (2 * math.pi * r)

    def update(self):

        self.GUI.pointers = [*map()]

