import cv2
from matplotlib import pyplot as plt
import numpy as np

PATH_in = "ProblemSets/ps1_python/input/"
PATH_out = "ProblemSets/ps1_python/output/"

img = cv2.imread(PATH_in + "ps1-input0.png", 0)

img2 = cv2.Canny(img, 100, 200)
img2 = img2 / 255.0
print img2[10]


plt.subplot(121)
plt.imshow(img, cmap="Greys_r")

plt.subplot(122)
plt.imshow(img2, cmap="Greys_r")
# plt.imsave(PATH_out+"ps1-1-a-1.png", img2, cmap="Greys_r")

plt.show()
