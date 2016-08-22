import cv2
from ps1_python.hough_lines import *
from matplotlib import pyplot as plt

PATH_in = "input/"
PATH_out = "output/"

img_origin = cv2.imread(PATH_in + "ps1-input0-noise.png", 0)

img_origin_canny = cv2.Canny(img_origin, 100, 100)

img_smooth = cv2.GaussianBlur(img_origin, (9, 9), 0)

img_smooth_canny = cv2.Canny(img_smooth, 150, 150)

img_nonoise = cv2.imread(PATH_in + "ps1-input0.png")

img_nonoise_canny = cv2.Canny(img_nonoise, 100, 100)

plt.subplot(321)
plt.imshow(img_origin, cmap="Greys_r")
plt.subplot(322)
plt.imshow(img_origin_canny, cmap="Greys_r")
#plt.imsave(PATH_out+"ps1-3-b-1.png", img_origin_canny, cmap="Greys_r")
plt.subplot(323)
plt.imshow(img_smooth, cmap="Greys_r")
plt.imsave(PATH_out+"ps1-3-a-1.png", img_smooth, cmap="Greys_r")
plt.subplot(324)
plt.imshow(img_smooth_canny, cmap="Greys_r")
plt.imsave(PATH_out+"ps1-3-b-2.png", img_smooth_canny, cmap="Greys_r")
plt.subplot(325)
plt.imshow(img_nonoise, cmap="Greys_r")
plt.subplot(326)
plt.imshow(img_nonoise_canny, cmap="Greys_r")

h, t, r = hough_lines_acc(img_smooth_canny)

peaks = hough_peaks(h, 6, threshold=50, neighborhood_size=20)

print peaks

plt.figure(3)
plt.imshow(h, cmap="coolwarm_r")

x_list = [x for (x,y) in peaks]
y_list = [y for (x,y) in peaks]

plt.plot(y_list, x_list, "ro")
plt.savefig(PATH_out + "ps1-3-c-1.png")


hough_lines_draw(img_smooth, PATH_out + "ps1-3-c-2.png", peaks)

plt.show()
