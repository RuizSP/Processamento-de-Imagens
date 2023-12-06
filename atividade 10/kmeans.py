import cv2 as cv
import numpy as np


def kmeans(img):
    z = img.reshape((-1,3))
    z = np.float32(z)
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 40, 0.1)
    k = 8
    _,labels, centroides = cv.kmeans (z, k, None, criteria, 40, cv.KMEANS_RANDOM_CENTERS)
    centroides = np.uint8(centroides)
    newimg = centroides[labels.flatten()]
    newimg = newimg.reshape((img.shape))

    return newimg
    pass

def main():
    imagem = cv.imread("img.jpg")
    newimg = kmeans(imagem)
    cv.imshow("Original", imagem)
    cv.imshow("kmeans", newimg)

    cv.waitKey(0)
    cv.destroyAllWindows()
    pass

if __name__ == "__main__":
    main()
