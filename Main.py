# Title of IA Solution
#  ______
# IDE - PyCharm Community Edition
# Python 3.6
# Platform - Windows, Mac Linux


from View import *
from Controller import *

Ctrl = Controller(GUI(500,500))
Ctrl.GUI.draw_grid(21, "black")
Ctrl.draw_arrows("blue")
Ctrl.place_wire(250, 250, 1, color="yellow")
Ctrl.update_grid()
Ctrl.GUI.show()