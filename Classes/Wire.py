# Title of IA Solution
#  ______
# IDE - PyCharm Community Edition
# Python 3.6
# Platform - Windows, Mac Linux

class Wire(object):

    def __init__(self, x, y, I, gui_sign):
        self.__x = x
        self.__y = y
        self.__I = I
        self.GUI_sign = gui_sign

    @property
    def I(self):
        return self.__I

    @I.setter
    def I(self,I):
        self.__I = I

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
