import numpy as np
import math

class FloatArray2D:
	def __init__(self, x_min, x_max, x_resolution, y_min, y_max, y_resolution):
		self.x_min = x_min
		self.x_max = x_max
		self.x_resolution = x_resolution
		self.y_min = y_min
		self.y_max = y_max
		self.y_resolution = y_resolution
		self.array = np.zeros((math.ceil((x_max - x_min) / x_resolution), math.ceil((y_max - y_min) / y_resolution)))
		print self.array.size

	def __getitem__(self, item):
		ix, iy = item

