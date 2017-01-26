# Title of IA Solution
#  ______
# IDE - PyCharm Community Edition
# Python 3.6
# Platform - Windows, Mac Linux

import math

class Pointer(object):

    def __init__(self, x, y, canvas, color,size):
        self.__direction = 0
        self.__x = x
        self.__y = y
        self.size = size
        self.__color = color
        self.canvas = canvas
        self.nodes = [(x, y - self.size / 2), (x + self.size / 3, y + self.size / 2), (x - self.size / 3, y + self.size / 2), (x, y - self.size / 2)]
        #[(x, y - self.ARROWSIZE / 2),(x + self.ARROWSIZE / 2, y + self.ARROWSIZE / 2), (x - self.ARROWSIZE / 2, y+ self.ARROWSIZE / 2),(x, y - self.ARROWSIZE / 2)]
        self.GUI_sign = canvas.create_line(self.nodes, fill=color)

    def rotate_pointer(self, angle):
        self.direction = (self.direction + angle) % 360
        angle = math.radians(angle)

        def mapper(cords):
            return self.__x + math.cos(angle) * (cords[0] - self.__x) - math.sin(angle) * (cords[1] - self.__y),self.__y + math.sin(angle) * (cords[0] - self.__x) + math.cos(angle) * (cords[1] - self.__y)

        self.nodes = [*map(mapper, self.nodes)]
        self.canvas.delete(self.GUI_sign)
        self.redraw()

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self,x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self,y):
        self.__y = y

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
            self.__direction = direction % 360

    def redraw(self):
        self.GUI_sign
        self.GUI_sign = self.canvas.create_line(self.nodes,fill = self.__color)
