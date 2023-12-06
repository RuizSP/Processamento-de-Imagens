import cv2 as cv
import numpy as np

def blendingMask(image1, image2, alpha):
	#addWeighted faz as misturas das imagens de acordo com pesos
	#alpha é o peso da imagem 1
	#1-alpha: peso da imagem2
	# desta forma quanto maior o alpha mais relevante será a imagem 1 para mistura e menos relevante será a 	
    return cv.addWeighted(image1, alpha, image2, 1 - alpha, 0)

def rescaleImage(imagem, percent):
    scaleFactor = percent / 100
    res = cv.resize(imagem, (int(imagem.shape[1] * scaleFactor), int(imagem.shape[0] * scaleFactor)))
    return res

def paste(src, dst, x, y):
    newImage = np.copy(dst)
    if x >= 0 and y >= 0:
        for i in range(0, src.shape[0]):
            for j in range(0, src.shape[1]):
                if i + y < newImage.shape[0] and j + x < newImage.shape[1]:
                    alpha = src[i, j, 3] / 255.0  # Valor de transparência no canal alfa (normalizado entre 0 e 1)
                    # o valor final dos pixels da nova imagem é calculado utilizando uma combinação ponderada. 
                    newImage[i + y, j + x, :3] = (1 - alpha) * newImage[i + y, j + x, :3] + alpha * src[i, j, :3]
                    # (1 - alpha) * newImage[i + y, j + x, :3] = quanto maior for o valor de alpha menor será a contribuição dos pixels no canal alpha da imagem 1
                    # alpha * src[i, j, :3] quanto maior o valor de alpha maior será a contribuição dos pixels da imagem 2
                    # as duas contribuições são somadas para obter o valor final do pixel na nova imagem;
                    
    else:
        print("X e Y devem ser valores maiores que 0")
    return newImage

def main():
    imagePath1 = "arara_azul.jpg"
    imagePath2 = "marca.png"
    image1 = cv.imread(imagePath1)
    image2 = cv.imread(imagePath2, cv.IMREAD_UNCHANGED)  # Carregar a imagem com canal alfa
    
    cv.imshow("Imagem Original", image1)
    cv.imshow("imagem maskHair", image2)
    
    image2 = rescaleImage(image2, 40)
    newimage = paste(image2, image1, 200, 500)
    newImg = blendingMask(image1, newimage, 0.8)

    cv.imshow("Nova imagem", newImg)
    cv.imwrite("img_marcadagua.png", newImg)
    cv.waitKey(0)

if __name__ == "__main__":
    main()

