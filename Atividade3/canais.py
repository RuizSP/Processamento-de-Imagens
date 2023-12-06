import cv2 as cv
import numpy as np

def splitChannels(image):
    blueChannel, greenChannel, redChannel = cv.split(image)
    imageBlue = cv.merge([blueChannel, np.zeros_like(blueChannel), np.zeros_like(blueChannel)])
    imageGreen = cv.merge([np.zeros_like(greenChannel), greenChannel, np.zeros_like(greenChannel)])
    imageRed = cv.merge([np.zeros_like(redChannel), np.zeros_like(redChannel), redChannel])
    
    return imageBlue, imageGreen, imageRed

def calcMean(image, channel):
    pixelSum = np.sum(image[:, :, channel])
    pixelNumber = image.shape[0] * image.shape[1]
    
    return pixelSum / pixelNumber

def maxChannel(mediaBlue, mediaGreen, mediaRed):
    max_media = max(mediaBlue, mediaGreen, mediaRed)
    if max_media == mediaBlue:
        return "O canal azul é predominante"
    elif max_media == mediaGreen:
        return "O canal verde é predominante"
    else:
        return "O canal vermelho é predominante"

def main():
    image = cv.imread("rickpicles.jpeg")
    cv.imshow("imagem", image)
    b, g, r = splitChannels(image)
    cv.imshow("b", b)
    cv.imshow("g", g)
    cv.imshow("r", r)
    
    mediaBlue = calcMean(b, 0)
    mediaGreen = calcMean(g, 1)
    mediaRed = calcMean(r, 2)
    
    print(f"Média do canal B: {mediaBlue}\nMédia do canal G: {mediaGreen}\nMédia do canal R: {mediaRed}")
    print(maxChannel(mediaBlue, mediaGreen, mediaRed))
    
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()

