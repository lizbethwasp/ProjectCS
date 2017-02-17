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

    grid = {}

    # Initialization of the class Controller
    def __init__(self, GUI):
        self.GUI = GUI
        self.GUI.canvas.bind("<Button-1>", lambda event: self.detect_wire(event))
        self.GUI.canvas.bind("<B1-Motion>", lambda event: self.move_wire(event))
        self.GUI.canvas.bind("<Button-2>", lambda event: self.place_wire(event.x, event.y, 0, color="Red", size=15))
        self.GUI.scale.bind("<B1-Motion>",self.update_wire_I)
        self.GUI.delButton["command"] = self.delete_wire
        self.active_wire = 0

    #An Event handler which deletes a selected wire object.
    # Fires on when "Delete" button is pressed
    def delete_wire(self):
        print("Del wire")
        if self.active_wire:
            self.active_wire.destroy()
            self.wires.remove(self.active_wire)
            self.update_grid()

    #An Event handler which updates field I of a selected wire object according to "Scale" Widget (Scroll bar) value.
    # Fires on by change in value of "Scale" Widget.
    def update_wire_I(self, event):
        if self.active_wire:
            self.active_wire.I = self.GUI.scale.get()
            self.update_grid()
            print("Wire I changed")

    #An Event handler which sets the wire, which is being the closest to the place of click, active.
    #  Fires on by the click on "Canvas" Widget.
    def detect_wire(self, event):
        for wire in self.wires:
            if wire.GUI_sign in event.widget.find_closest(event.x, event.y):
                self.active_wire = wire
                print("Wire detected")
                self.GUI.scale.set(self.active_wire.I)

    #An Event handler which resets active wire's X and Y coordinates according to the location of mouse pointer and updates the view.
    #  Fires on when the mouse pointer is moving with left button being pressed.
    def move_wire(self, event):
        if self.active_wire:
            self.active_wire.x = event.x
            self.active_wire.y = event.y
            self.active_wire.redraw()
            self.update_grid()
            print("Wire transited")

    #A Method, which creates a new wire with given parameters.
    def place_wire(self, x, y, I, color, size):
        print("Wire placed")
        self.wires.append(Wire(x, y, I, color, size, self.GUI.canvas))
        self.active_wire = self.wires[-1]
        self.update_grid()

    #A Method, which draws arrows on the point of intersection of vertical and horizontal lines.
    # The method is to be called one time after drawing grid.
    def draw_arrows(self, color):
        ppgv = self.GUI.canvas_width / len(self.grid['v'])  # Pointers per grid vertical
        ppgh = self.GUI.canvas_height / len(self.grid['h'])  # Pointers per grid horizontal

        if len(self.grid) == 0:
            raise Exception("Draw Grid first")

        for x in (range(1, len(self.grid['h']))):
            for y in (range(1, len(self.grid['v']))):
                self.pointers.append(Pointer(x * ppgh, y * ppgv, self.GUI.canvas, color=color, size=15))

    #A Method which calculates the magnetic field force with given parameters.
    def mag_field_force(self, I, r):
        return I / (2 * math.pi * r)

    #A Method which calculates the angle using coordinates of triangle's verteces.
    def calc_angle(self, p0, p1, p2):
        a = (p1[0] - p0[0]) ** 2 + (p1[1] - p0[1]) ** 2
        b = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        c = (p2[0] - p0[0]) ** 2 + (p2[1] - p0[1]) ** 2
        in_rad = math.acos((a + b - c) / math.sqrt(4 * a * b))
        if p2[0] < p0[0] or p2[1] < p0[1]:
            return 360 - int(in_rad * 180 / math.pi)
        return int(in_rad * 180 / math.pi)

    #A Method which calculates the value of wire's influence on a pointer.
    def calc_power(self, pointer, wire):
        distance = math.sqrt((pointer.x - wire.x) ** 2 + (pointer.y - wire.y) ** 2)
        return self.mag_field_force(wire.I, distance)

    #A Method which draws a grid and fills self.v, self.h in with indexes of vertical and horizontal lines.
    def draw_grid(self, line_number, color):

        if len(self.grid) != 0:
            raise Exception("Must be only one Grid")

        g = {}
        v = []
        h = []

        for x in range(line_number):
            v.append(self.GUI.canvas.create_line(0, (self.GUI.canvas_width / line_number) * x,
                                             self.GUI.canvas_width,
                                             (self.GUI.canvas_width / line_number) * x, fill=color))
            h.append(self.GUI.canvas.create_line((self.GUI.canvas_width / line_number) * x, 0,
                                             (self.GUI.canvas_width / line_number) * x,
                                                 self.GUI.canvas_width, fill=color))

        g["h"] = h
        g["v"] = v
        self.grid = g

    #A Method which calculates the value of wire's influence on pointers and rotates them.
    # The method also redraws the wires.
    def update_grid(self):
        print("Upd grid...")
        for ptr in range(len(self.pointers)):
            self.pointers[ptr].rotate_to_0()
        for wire in self.wires:
            power_lambda = lambda x: self.calc_power(x, wire)
            angles_lambda = lambda x: self.calc_angle([wire.x, wire.y -
                                                       math.sqrt((x.x - wire.x) ** 2 +
                                                                 (x.y - wire.y) ** 2)], [wire.x, wire.y],
                                                      [x.x, x.y])
            powers = [*map(power_lambda, self.pointers)]
            angles = [*map(angles_lambda, self.pointers)]
            for ptr in range(len(self.pointers)):
                cur_ptr = self.pointers[ptr]
                if math.fabs(powers[ptr]) > 0.001:
                    if int(cur_ptr.direction) == 90:
                        cur_ptr.rotate_pointer(
                            angles[ptr])
                    else:
                        cur_ptr.rotate_pointer(
                            angles[ptr])
                elif powers[ptr] < -0.001:
                    if int(cur_ptr.direction) == 90:
                        cur_ptr.rotate_pointer(
                            cur_ptr.direction)
                    else:
                        cur_ptr.rotate_pointer(
                            angles[ptr])
        for wire in self.wires:
            wire.redraw()
