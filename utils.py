import numpy as np
import cv2

def get_limits(color):
    c= np.uint8([[color]])

    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    h = hsvC[0][0][0]

    lowerlimit = h - 10, 100, 100
    upperlimit = h + 10, 255, 255

    lowerlimit = np.array(lowerlimit, dtype=np.uint8)
    upperlimit = np.array(upperlimit, dtype=np.uint8)

    return lowerlimit, upperlimit