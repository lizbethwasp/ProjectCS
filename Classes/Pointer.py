# @author Veranika Boukun
# @date May 2017
# Siauliai Dizdvaris Gymnazium
# Magnetic Field Simulation
# Pointer.by
# IDE - PyCharm Community Edition
# Python 3.6.0
# Platform - PC

import math
import tkinter


class Pointer(object):

    #A Constructor of Pointer class which creates GUI represrntation of a pointer.
    def __init__(self, x, y, canvas, color, size):
        self.__direction = 90
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.canvas = canvas
        self.nodes = [(x-size, y), (x+size, y)]
        self.GUI_sign = canvas.create_line(self.nodes, fill=color, arrow=tkinter.FIRST,
                                           arrowshape=[2 * size - size // 2,
                                                       2 * size, size // 2])

    #A Method which rotates pointer to the default direction
    def rotate_to_0(self):
        self.direction = 90
        self.nodes = [(self.x-self.size, self.y), (self.x+self.size, self.y)]
        self.redraw()

    #A Method whcih rotates pointers on a given ammount of degrees
    def rotate_pointer(self, angle):
        self.direction += angle
        angle = math.radians(angle)

        def mapper(cords):
            return self.x + math.cos(angle) * (cords[0] - self.x) - math.sin(angle) * (cords[1] - self.y), \
                   self.y + math.sin(angle) * (cords[0] - self.x) + math.cos(angle) * (cords[1] - self.y)

        self.nodes = [*map(mapper, self.nodes)]
        self.redraw()

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
            self.__direction = direction % 360 #Taking the remainder of division to prevent Integer overflow

    #A Method which deletes the current GUI represrntation, and than draws it again
    def redraw(self):
        self.canvas.delete(self.GUI_sign)
        self.GUI_sign = self.canvas.create_line(self.nodes, fill=self.color, arrow=tkinter.FIRST,
                                                arrowshape=[2 * self.size - self.size // 2,
                                                            2 * self.size, self.size // 2])
