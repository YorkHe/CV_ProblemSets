import cv2
from matplotlib import pyplot as plt
import numpy as np
import os

PATH = "ProblemSets/ps0_python/output/"

img = cv2.cvtColor(cv2.imread(PATH+"ps0-1-a-1.png"), cv2.COLOR_BGR2RGB)


# cv2.imwrite(PATH+"ps0-2-a-1.png", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
img2 = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
# plt.imsave(PATH+("ps0-2-a-1.png"), img2)

r,g,b = cv2.split(img)


plt.axis("off")

plt.subplot(231)
plt.imshow(img)

plt.subplot(232)
plt.imshow(img2)

plt.subplot(234)
plt.imshow(r, cmap="Greys_r")
plt.imsave(PATH+("ps0-2-c-1.png"), r, cmap="Greys_r")

plt.subplot(235)
plt.imshow(g, cmap="Greys_r")
plt.imsave(PATH+("ps0-2-b-1.png"), g, cmap="Greys_r")

plt.subplot(236)
plt.imshow(b, cmap="Greys_r")


plt.show()
