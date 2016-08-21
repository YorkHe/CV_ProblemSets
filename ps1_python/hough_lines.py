import cv2
from matplotlib import pyplot as plt
from matplotlib import pylab as pl
from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure, binary_erosion
import numpy as np
import math


PATH_out = "ProblemSets/ps1_python/output/"

def hough_accumulator(BM, rhoResolution=1, theta=range(0, 180, 1)):
    rows, cols = BM.shape
    H = np.zeros((2*(rows+cols), len(theta)))
    cos_d = []
    sin_d = []

    for t in theta:
        cos_d.append(math.cos(math.radians(t)))
        sin_d.append(math.sin(math.radians(t)))

    for x in range(rows):
        for y in range(cols):
            if (BM[x,y] != 0):
                for t in range(len(theta)):
                    d = int(x * cos_d[t] - y * sin_d[t])
                    H[d+(rows+cols),t] += 1

    return (H, theta, rhoResolution)

def hough_peaks(acc, num):
    acc = cv2.GaussianBlur(acc, (17,17), 0)
    arr = []
    for (x, y), value in np.ndenumerate(acc):
        arr.append(((x,y),value))

    arr.sort(reverse=True, key= lambda value: value[1])

    return [i[0] for i in arr[:num]]

def hough_lines_draw(img, outname, peaks, rhoResolution=1, theta=range(0, 180, 1)):
    row, col = img.shape
    plt.figure(2)
    plt.imshow(img, cmap="Greys_r")
    for (d, t) in peaks:
        if math.fabs(math.sin(math.radians(t))) > 0.1:
            x = range(row)
            y = [1/math.sin(math.radians(t))* (math.cos(math.radians(t))* i - (d-row-col)) for i in x]
            plt.plot(x, y)
        else:
            plt.vlines((d-row-col), ymin=0, ymax=row)

    plt.savefig(PATH_out + outname)
    plt.show()


if __name__ == '__main__':
    # PATH_in = "ProblemSets/ps1_python/input/"
    PATH_in = "ProblemSets/ps1_python/output/"
    #img = cv2.imread(PATH_in + "ps1-input0.png", 0)
    img = cv2.imread(PATH_in + "ps1-3-a-1.png", 0)
    img2 = cv2.Canny(img, 150, 150)
    h, t, r = hough_accumulator(img2)

    peaks = hough_peaks(h, 16)

    print (peaks)

    plt.figure(3)
    plt.imshow(h, cmap="coolwarm_r")

    plt.plot(*zip(*peaks), marker="o", color="r")
    plt.savefig(PATH_out+"ps1-3-c-1.png")

    hough_lines_draw(img, outname="ps1-3-c-2.png", peaks=peaks)


    # plt.figure(num=2, figsize=(1000,1000), dpi=200)
    # plt.figure(2)
    # plt.imshow(h, cmap="coolwarm_r")
    # plt.show()
