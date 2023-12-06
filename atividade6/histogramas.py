import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import Showgraphics as sg

def grayHistogram(image):
    hist = cv.calcHist([image], [0], None, [256], [0, 256])
    return hist

def colorHistogram(image):
    hist_channels = []
    colors = ('b', 'g', 'r')
    
    for i, color in enumerate(colors):
        channel_hist = cv.calcHist([image], [i], None, [256], [0, 256])
        hist_channels.append(channel_hist)
    
    return hist_channels


def main():
    img = cv.imread("lontra.jpeg")
    imgCopy = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    histGray = grayHistogram(imgCopy)
    hist_channels = colorHistogram(img)
    sg.plotGraphics(img, imgCopy, histGray, hist_channels)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
