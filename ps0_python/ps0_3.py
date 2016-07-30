import cv2
from matplotlib import pyplot as plt
import numpy as np

PATH = "ProblemSets/ps0_python/output/"

img1 = cv2.cvtColor(cv2.imread(PATH + "ps0-1-a-1.png"), cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(cv2.imread(PATH + "ps0-1-a-2.png"), cv2.COLOR_BGR2RGB)

img1_width, img1_height = img1.shape[:2]
img2_width, img2_height = img2.shape[:2]

print (img1_width, img1_height)
print (img2_width, img2_height)

img3 = img2.copy()

img1_start_x = img1_width / 2 - 50
img1_start_y = img1_height / 2 - 50

img2_start_x = img2_width / 2 - 50
img2_start_y = img2_height / 2 - 50

img3[img2_start_x:img2_start_x+100, img2_start_y:img2_start_y+100] = \
    img1[img1_start_x:img1_start_x+100, img1_start_y: img1_start_y+100]



plt.axis("off")
plt.subplot(131)
plt.imshow(img1)

plt.subplot(132)
plt.imshow(img2)

plt.subplot(133)
plt.imshow(img3)
plt.imsave(PATH+"ps0-3-a-1.png", img3)

plt.show()
