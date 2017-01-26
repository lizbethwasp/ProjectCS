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
Ctrl.place_wire(200, 200, 1, color="yellow")
Ctrl.place_wire(300, 300, -1, color="green")
Ctrl.update_grid()
Ctrl.GUI.show()