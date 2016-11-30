class Pointer(object):

    def __init__(self, x, y, direction, index):
        self.__direction = direction % 360
        self.__x = x
        self.__y = y
        self.__index = index

	def draw(canvas,x = self.x, y = self.y):
		canvas.draw_line()

	@property
	def index(self):
		return self.__index

	@index.setter
	def index(self,index):
		self.__index = index

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self,x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self,y):
        self.__y = y

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction):
            self.__direction = direction % 360
