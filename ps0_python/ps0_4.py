import cv2
from matplotlib import pyplot as plt
import numpy as np
from scipy.ndimage.interpolation import shift

PATH = "ProblemSets/ps0_python/output/"

img = cv2.cvtColor(cv2.imread(PATH+"ps0-1-a-1.png"), cv2.COLOR_BGR2RGB)

r,g,b = cv2.split(img)

print np.min(g), np.max(g), np.mean(g), np.std(g)

img2 = g.copy()

mean = np.mean(g)
standrad = np.std(g)

plt.axis("off")

plt.subplot(141)
plt.imshow(g[:], cmap="Greys_r")

img2[:] = (((img2[:] - mean)/standrad) * 10) + mean


print g
print img2

plt.subplot(142)
plt.imshow(img2, cmap="Greys_r")
plt.imsave(PATH+"ps0-4-b-1.png", img2, cmap="Greys_r")

rows, cols = g.shape

M = np.float32([[1,0,-2],[0,1,0]])

img3 = cv2.warpAffine(g, M, (cols, rows))

print img3

plt.subplot(143)
plt.imshow(img3, cmap="Greys_r")
plt.imsave(PATH+"ps0-4-c-1.png", img3, cmap="Greys_r")

img4 = g - img3

plt.subplot(144)
plt.imshow(img4, cmap="Greys_r")
plt.imsave(PATH+"ps0-4-d-1.png", img4, cmap="Greys_r")


plt.show()
