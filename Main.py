# Title of IA Solution
#  ______
# IDE - PyCharm Community Edition
# Python 3.6
# Platform - Windows, Mac Linux


from View import *
from Controller import *

Ctrl = Controller(GUI(500, 500))
Ctrl.GUI.draw_grid(21, "black")
Ctrl.draw_arrows("blue")
Ctrl.place_wire(200, 200, 1, color="Yellow", size=10)
Ctrl.place_wire(300, 300, -1, color="Green", size=10)
Ctrl.update_grid()
Ctrl.GUI.show()
