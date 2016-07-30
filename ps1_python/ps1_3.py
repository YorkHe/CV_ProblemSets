import cv2
from matplotlib import pyplot as plt

PATH_in = "ProblemSets/ps1_python/input/"
PATH_out = "ProblemSets/ps1_python/output/"

img_origin = cv2.imread(PATH_in + "ps1-input0-noise.png")

img_origin_canny = cv2.Canny(img_origin, 100, 100)

img_smooth = cv2.GaussianBlur(img_origin, (5, 5), 10)

img_smooth_canny = cv2.Canny(img_smooth, 150, 150)

img_nonoise = cv2.imread(PATH_in + "ps1-input0.png")

img_nonoise_canny = cv2.Canny(img_nonoise, 100, 100)

plt.subplot(321)
plt.imshow(img_origin)
plt.subplot(322)
plt.imshow(img_origin_canny)
#plt.imsave(PATH_out+"ps1-3-b-1.png", img_origin_canny, cmap="Greys_r")
plt.subplot(323)
plt.imshow(img_smooth)
#plt.imsave(PATH_out+"ps1-3-a-1.png", img_smooth, cmap="Greys_r")
plt.subplot(324)
plt.imshow(img_smooth_canny)
#plt.imsave(PATH_out+"ps1-3-b-2.png", img_smooth_canny, cmap="Greys_r")
plt.subplot(325)
plt.imshow(img_nonoise)
plt.subplot(326)
plt.imshow(img_nonoise_canny)

plt.show()
