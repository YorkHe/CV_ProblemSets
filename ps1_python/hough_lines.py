import cv2
from matplotlib import pyplot as plt
import numpy as np
import math
import scipy.ndimage.filters as filters
import scipy.ndimage as ndimage

def hough_lines_acc(BW, rho_resolution=1.0, theta=range(0, 180, 1)):
	rows, cols = BW.shape
	H = np.zeros((4*(max(rows,cols)), len(theta)))
	cos_d = []
	sin_d = []

	for t in theta:
		cos_d.append(math.cos(math.radians(t)))
		sin_d.append(math.sin(math.radians(t)))

	for x in range(rows):
		for y in range(cols):
			if (BW[x, y] != 0):
				for t in range(len(theta)):
					d = x * cos_d[t] - y * sin_d[t]
					H[d + 2 * (max(rows, cols)),t] += 1

	return (H, theta, rho_resolution)

def hough_peaks(acc, num, threshold = 60, neighborhood_size = 10):
	data_max = filters.maximum_filter(acc, neighborhood_size)
	maxima = (acc == data_max)

	data_min = filters.minimum_filter(acc, neighborhood_size)
	diff = ((data_max - data_min) > threshold)
	maxima[diff == 0] = 0

	labeled, num_objects = ndimage.label(maxima)
	slices = ndimage.find_objects(labeled)

	x, y = [], []

	for dx, dy in slices:
		x_center = (dx.start + dx.stop - 1) / 2
		x.append(x_center)
		y_center = (dy.start + dy.stop - 1) / 2
		y.append(y_center)

	return [(xx,yy) for (xx,yy) in zip(x,y)][:num]

def hough_lines_draw(img, outname, peaks, rhoResolution=1.0, theta=range(0, 180, 1)):
	plt.figure(2)
	print img.shape
	row, col = img.shape
	plt.imshow(img, cmap="Greys_r")
	for (d, t) in peaks:
		if math.fabs(math.sin(math.radians(t))) > 0.1:
			x = range(row)
			y = [1/math.sin(math.radians(t))* (math.cos(math.radians(t))* i - (d-row-col)) for i in x]
			plt.plot(x, y, color="red")
		else:
			plt.vlines(abs(d-row-col), ymin=0, ymax=row, color="red")

	plt.savefig(outname)
	plt.show()


if __name__ == '__main__':
	PATH_in = "input/"
	PATH_out = "output/"
	img = cv2.imread(PATH_in + "ps1-input0.png", 0)
	img2 = cv2.Canny(img, 150, 150)

	h, t, r = hough_lines_acc(img2)

	print h.shape

	plt.subplot(111)
	plt.imshow(h, cmap="coolwarm_r")
	plt.imsave(PATH_out + "ps1-2-a-1.png", h, cmap="coolwarm_r")

	peaks = hough_peaks(h, 10)
	print peaks

	x_list = [x for [x,y] in peaks]
	y_list = [y for [x,y] in peaks]

	plt.plot(y_list, x_list, "ro")

	plt.savefig(PATH_out + "ps1-2-b-1.png", cmap="coolwarm-r")

	# plt.show()

	hough_lines_draw(img, outname=PATH_out + "ps1-2-c-1.png", peaks=peaks, rhoResolution=r, theta=t)

	plt.show()
