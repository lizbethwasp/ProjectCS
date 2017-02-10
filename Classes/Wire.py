# Title of IA Solution
#  ______
# IDE - PyCharm Community Edition
# Python 3.6
# Platform - Windows, Mac Linux


class Wire(object):

    #Constructor of Wire class, draw GUI representation of wire
    def __init__(self, x, y, I, color, size, canvas):
        self.x = x
        self.y = y
        self.I = I
        self.color = color
        self.size = size
        self.canvas = canvas

        if self.I > 0:
            self.direction_sign = canvas.create_oval(x + size // 2, y + size // 2, x - size // 2, y - size // 2,
                                                     fill="black")
        else:
            self.direction_sign = canvas.create_line([(x, y), (x + size // 2, y + size // 2), (x, y), (x - size // 2,
                                                                                                       y - size // 2),
                                                      (x, y), (x - size // 2, y + size // 2),
                                                      (x, y), (x + size // 2, y - size // 2)], fill="black")

        self.GUI_sign = canvas.create_oval(x+size, y+size, x-size, y-size, fill=color)
        self.canvas.itemconfig(self.GUI_sign, tags="wire" + str(self.GUI_sign))

    #Method, delete GUI representation of wire
    def destroy(self):
        self.canvas.delete(self.GUI_sign)
        self.canvas.delete(self.direction_sign)

    #Method, delete current GUI representation of wire and draw it again
    def redraw(self):
        self.canvas.delete(self.GUI_sign)
        self.canvas.delete(self.direction_sign)
        self.GUI_sign = self.canvas.create_oval(self.x+self.size, self.y+self.size, self.x-self.size, self.y-self.size,
                                                fill=self.color)
        if self.I > 0:
            self.direction_sign = self.canvas.create_oval(self.x + self.size // 2, self.y + self.size // 2,
                                                          self.x - self.size // 2, self.y - self.size // 2,
                                                          fill="black")
        else:
            self.direction_sign = self.canvas.create_line([(self.x, self.y), (self.x + self.size // 2,
                                                                              self.y + self.size // 2),
                                                           (self.x, self.y),
                                                           (self.x - self.size // 2, self.y - self.size // 2),
                                                           (self.x, self.y), (self.x - self.size // 2,
                                                                              self.y + self.size // 2),
                                                           (self.x, self.y), (self.x + self.size // 2,
                                                                              self.y - self.size // 2)], fill="black")
