import tkinter

class GUI:

	def __init__(self, canvas_lenght):
		self.canvas_lenght = canvas_lenght
		self.root = tkinter.Tk()
		self.canvas = tkinter.Canvas(self.root, width=canvas_lenght, height=canvas_lenght)

	def draw_grid(self,line_number, color):
		g = {}  # Grid
		v = []  # Verticals
		h = []  # Horizontals
		for x in range(24):
			v.append(self.canvas.create_line(0, (self.canvas_lenght / line_number) * (x), self.canvas_lenght, (self.canvas_lenght / line_number) * (x), fill=color))
			h.append(self.canvas.create_line((self.canvas_lenght / line_number) * (x), 0, (self.canvas_lenght / line_number) * (x), self.canvas_lenght, fill=color))
		g["h"] = h
		g["v"] = v
		return g

	def show(self):
		self.canvas.pack()
		self.root.mainloop()

