import cv2 as cv
import numpy as np


def equalizeHist(image):
    imgHSV = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    imgHSV[:,:, 2] = cv.equalizeHist(imgHSV[:,:,2])
    output = cv.cvtColor(imgHSV, cv.COLOR_HSV2BGR)
    return  output


