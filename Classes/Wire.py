# Title of IA Solution
# Wire.by
# IDE - PyCharm Community Edition
# Python 3.6.0
# Platform - PC


class Wire(object):

    #A Constructor of Wire class which draws GUI representation of a wire
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

    #A Method which deletes GUI representation of a selected wire
    def destroy(self):
        self.canvas.delete(self.GUI_sign)
        self.canvas.delete(self.direction_sign)

    #A Method which deletes the current GUI representation of a wire and draws it again
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
