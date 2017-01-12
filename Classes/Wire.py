class Wire(object):

    def __init__(self, x, y, I):
        self.__x = x
        self.__y = y

    @property
    def I(self):
        return self.__I

    @I.setter
    def I(self,I):
        self.__I = I / 1.0


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
