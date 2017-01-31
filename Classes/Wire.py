# Title of IA Solution
#  ______
# IDE - PyCharm Community Edition
# Python 3.6
# Platform - Windows, Mac Linux



class Wire(object):

    def __init__(self, x, y, I, color, size, canvas):
        self.__x = x
        self.__y = y
        self.__I = I
        self.color = color
        self.size = size
        self.canvas = canvas
        self.GUI_sign = canvas.create_oval(x+size, y+size, x-size, y-size, fill=color)
        self.canvas.itemconfig(self.GUI_sign, tags= "wire" + str(self.GUI_sign))


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

    def redraw(self):
        self.canvas.delete(self.GUI_sign)
        self.GUI_sign = self.canvas.create_oval(self.x+self.size, self.y+self.size, self.x-self.size, self.y-self.size, fill=self.color)