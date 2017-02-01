# Title of IA Solution
# Pointer.by
# IDE - PyCharm Community Edition
# Python 3.6.0
# Platform - PC

import math
import tkinter


class Pointer(object):

    def __init__(self, x, y, canvas, color, size):
        self.__direction = 0
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.canvas = canvas
        self.nodes = [(x, y+size), (x, y-size)]
        self.GUI_sign = canvas.create_line(self.nodes, fill=color, arrow=tkinter.FIRST,
                                           arrowshape=[2 * size - size // 2,
                                                       2 * size, size // 2])

    def rotate_to_0(self):
        self.direction = 0
        self.nodes = [(self.x, self.y+self.size), (self.x, self.y-self.size)]
        self.redraw()

    def rotate_pointer(self, angle):
        self.direction = (self.direction + angle) % 360
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
            self.__direction = direction % 360

    def redraw(self):
        self.canvas.delete(self.GUI_sign)
        self.GUI_sign = self.canvas.create_line(self.nodes, fill=self.color, arrow=tkinter.FIRST,
                                                arrowshape=[2 * self.size - self.size // 2,
                                                            2 * self.size, self.size // 2])
