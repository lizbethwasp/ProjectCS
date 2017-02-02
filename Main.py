# Title of IA Solution
# Main.by
# IDE - PyCharm Community Edition
# Python 3.6.0
# Platform - PC


from View import *
from Controller import *

Ctrl = Controller(GUI(500, 500))
Ctrl.draw_grid(21, "black")
Ctrl.draw_arrows("blue")
Ctrl.update_grid()
Ctrl.GUI.show()
