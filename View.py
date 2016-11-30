import tkinter
import math

def draw_arrow(target_canvas, x, y):
	return target_canvas.create_line([x, y, x - 10, y + 15, x - 5, y + 15, x - 5, y + 25, x + 5, y + 25, x + 5, y + 15,
									 x + 10, y + 15, x, y], fill="red")

def draw_rotated_arrow(target_canvas, x, y):
	cos = math.cos(20)
	sin = math.sin(20)
	return target_canvas.create_line([x, y, x - 10, y + 15, x - 5, y + 15, x - 5, y + 25, x + 5, y + 25, x + 5, y + 15,
									 x + 10, y + 15, x, y], fill="red")

def rotate_arrow(canvas, arrow, angle):
	coords = canvas.coords(arrow)
	print(coords)
	i = 0
	X=[]
	Y=[]
	while i < len(coords):
		if(i % 2 == 0):
			X.append(coords[i])
		else:
			Y.append(coords[i])
	R = coords[0] + coords[1]
	print(X)
	print(Y)
	print(R)
	# sin(angle) * R
	# cos(angle) * R

window = tkinter.Tk()
canvas = tkinter.Canvas(window,width=500,height=500)
arrow = canvas.coords(draw_arrow(canvas,100,100))
canvas.pack()
window.mainloop()