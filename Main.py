# Title of IA Solution
#  ______
# IDE - PyCharm Community Edition
# Python 3.6
# Platform - Windows, Mac Linux


from View import *
from Controller import *

Ctrl = Controller(GUI(500,500))
Ctrl.GUI.draw_grid(25, "black")
Ctrl.draw_arrows("red")
Ctrl.place_wire(250, 250, 10, color="red")
Ctrl.GUI.show()