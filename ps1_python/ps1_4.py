import cv2
from ps1_python.hough_lines import *
from matplotlib import pyplot as plt

PATH_in = "input/"
PATH_out = "output/"

img_origin = cv2.imread(PATH_in + "ps1-input1.png")

img_gray = cv2.cvtColor(img_origin, cv2.COLOR_BGR2GRAY)

img_gray_canny= cv2.Canny(img_gray, 150, 150)

img_smooth = cv2.GaussianBlur(img_gray, (9,9), 0)

img_smooth_canny = cv2.Canny(img_smooth, 150, 150)

plt.subplot(221)
plt.imshow(img_gray, cmap="Greys_r")

plt.subplot(222)
plt.imshow(img_gray_canny, cmap="Greys_r")

plt.subplot(223)
plt.imshow(img_smooth, cmap="Greys_r")
plt.imsave(PATH_out+"ps1-4-a-1.png", img_smooth, cmap="Greys_r")

plt.subplot(224)
plt.imshow(img_smooth_canny, cmap="Greys_r")
plt.imsave(PATH_out+"ps1-4-b-1.png", img_smooth_canny, cmap="Greys_r")

h,t,r = hough_lines_acc(img_smooth_canny)

peaks = hough_peaks(h, 4, threshold=20, neighborhood_size=10)

print peaks

plt.figure(3)
plt.imshow(h, cmap="coolwarm_r")

x_list = [x for (x,y) in peaks]
y_list = [y for (x,y) in peaks]

plt.plot(y_list, x_list, "ro")
plt.savefig(PATH_out + "ps1-4-c-1.png")


hough_lines_draw(img_origin, PATH_out + "ps1-4-c-2.png", peaks)

plt.show()






