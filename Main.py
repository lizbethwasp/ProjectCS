from View import *
from Controller import *

Ctrl = Controller(GUI(500))
Ctrl.GUI.draw_grid(24, "black")
Ctrl.place_wire(250, 250, 10, color="red")
Ctrl.GUI.show()
