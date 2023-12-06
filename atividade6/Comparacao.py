import cv2 as cv
import numpy as np
import math as mt
import histogramas


def findImage(imgs):
    minDist = float('inf')
    minIndex = float('inf')
    img = None
    for i in range(1, len(imgs)):
        dist = calcDist(imgs[0], imgs[i])
        if dist < minDist:
            minDist = dist
            img = imgs[i]
    return img, minDist


def process(img):
    #img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hist1 = cv.calcHist(img,[0, 1, 2], None, [256 ,256, 256], [0,256, 0,256, 0,256] )
    cv.normalize(hist1, hist1, 0, 1, cv.NORM_MINMAX)
    return hist1


def calcDist(img1, img2):
    hist1 = process(img1)
    hist2 = process(img2)
    cor, bt, chi = compareHist(hist1, hist2)
    return mt.sqrt(((1-cor)**2) + (chi**2) + (bt**2))


def compareHist(hist1, hist2):
    return cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL),cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA),  cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)


def main():
    images = [cv.imread("s1.jpg"), cv.imread("d2.jpeg"), cv.imread("s2.jpg"), cv.imread("d1.jpg"), cv.imread("d3.jpg")]
    img, dist = findImage(images)
    print("a menor distancia é: ", dist)
    cv.imshow("Imagem com menor distancia", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
