import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import histogramas as hist
import Showgraphics as sg

def equalizeHist(image):
    imgHSV = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    imgHSV[:,:, 2] = cv.equalizeHist(imgHSV[:,:,2])
    output = cv.cvtColor(imgHSV, cv.COLOR_HSV2BGR)
    return  output

def main():
    img = cv.imread("jetson.png")
    newimg = equalizeHist(img)
    hist1 =hist.colorHistogram(img)
    hist2 =hist.colorHistogram(newimg)
    sg.plotGraphics2(img, newimg, hist1, hist2)
    cv.waitKey(0)
    cv.destroyAllWindows() 

if __name__ == "__main__":
    main()
