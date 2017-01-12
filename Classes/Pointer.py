import math


class Pointer(object):

    def __init__(self, x, y, direction, height, width):
        self.__direction = direction % 360
        self.__x = x
        self.__y = y
        self.nodes = [(x, y-5), (x, y+5), (x+1, y+1.5), (x-1, y+1.5)]

    def rotate_pointer(self, angle):
        self.direction  = (self.direction + angle) % 360
        angle = math.radians(angle)

        def mapper(cords):
            return(self.__x + math.cos(angle) * (cords[0] - self.__x) - math.sin(angle) * (cords[1] - self.__y),self.__y + math.sin(angle) * (cords[0] - self.__x) + math.cos(angle) * (cords[1] - self.__y))

        self.nodes = [*map(mapper, self.nodes)]

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self,index):
        self.__index = index

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
