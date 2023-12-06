import cv2 as cv
import numpy as np

def blendingMask(image1, image2, alpha):
	#addWeighted faz as misturas das imagens de acordo com pesos
	#alpha é o peso da imagem 1
	#1-alpha: peso da imagem2
	# desta forma quanto maior o alpha mais relevante será a imagem 1 para mistura e menos relevante será a 								 imagem 2
	return cv.addWeighted(image1, alpha , image2, 1-alpha, 0)





def main():
	imagePath1 = "Untitled.jpeg"
	imagePath2 = "Untitled2.jpg"
	image1 = cv.imread(imagePath1)
	image2 = cv.imread(imagePath2)
	 
	newImg = blendingMask(image1, image2, 0.5)
	cv.imshow("Imagem Original", image1)
	cv.imshow("imagem maskHair", image2)
	cv.imshow("Nova imagem", newImg)
	cv.waitKey(0)
	
	



if __name__ == "__main__":
	main()
