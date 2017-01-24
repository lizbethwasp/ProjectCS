import tkinter


class GUI:

	grid = {}

	def __init__(self, canvas_height, canvas_width):
		self.canvas_width = canvas_width
		self.canvas_height = canvas_height
		self.root = tkinter.Tk()
		self.canvas = tkinter.Canvas(self.root, width=canvas_width, height=canvas_height)

	def draw_grid(self,line_number, color):

		if (len(self.grid) != 0):
			raise Exception("Must be only one Grid");

		g = {}  # Grid
		v = []  # Verticals
		h = []  # Horizontals

		for x in range(line_number):
			v.append(self.canvas.create_line(0, (self.canvas_width / line_number) * (x), self.canvas_width, (self.canvas_width / line_number) * (x), fill=color))
			h.append(self.canvas.create_line((self.canvas_width / line_number) * (x), 0, (self.canvas_width / line_number) * (x), self.canvas_width, fill=color))

		g["h"] = h
		g["v"] = v
		self.grid = g


	def draw_pointer(self,pointer,color):
		self.canvas.create_line(pointer.nodes, fill = color)


	def show(self):
		self.canvas.pack()
		self.root.mainloop()