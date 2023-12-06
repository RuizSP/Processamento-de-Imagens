import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def grabCut(img, x , y , largura, altura):
    mask = np.zeros(img.shape[:2],np.uint8)
     # Definir retângulo inicial para o GrabCut
    rectGcut = (x, y, largura, altura)
     # Inicializar os arrays de máscara do GrabCut
    bgdModel = np.zeros((1,65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    cv.grabCut(img, mask, rectGcut, bgdModel, fgdModel, 5, cv.GC_INIT_WITH_RECT)
     # Modificar a máscara para que o fundo seja 0 ou 2, tornar o fundo preto
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8').astype("uint8")
     # Multiplicar a imagem original pela máscara para obter a imagem sem fundo
    result = img * mask2[:, :, np.newaxis]
    cv.imshow("Sem fundo", result)
    cv.waitKey(0)
    return result

def blur(img):
    ksize = (15, 15)
    sigma = 5 
    blurredImage = cv.GaussianBlur(img, ksize, sigma)
    blurredImage = cv.GaussianBlur(blurredImage, ksize, sigma)
    return blurredImage

def paste(src, dst, x, y):
    newImage = src
    if x >= 0 and y >= 0:
        for i in range(0, dst.shape[0]):
            for j in range(0, dst.shape[1]):
                if i + y < newImage.shape[0] and j + x < newImage.shape[1]:
                    # Adicionar condição para verificar se a cor do pixel em dst não é preta
                    if not np.all(dst[i][j] == 0):
                        newImage[i + y, j + x] = dst[i][j]
    else:
        print("X e Y devem ser valores maiores que 0")
    return newImage


def borradorDeFundo(img):
    imgNoBackground = grabCut(img, 215,0 , 285, 250 )
    imgBlur= blur(img)
    result = paste(imgBlur, imgNoBackground, 0, 0)
    
    return result

def main():
    imagem = cv.imread("img.jpg")
    imgBlur = borradorDeFundo(imagem)
    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1), plt.imshow(cv.cvtColor(imagem, cv.COLOR_BGR2RGB)), plt.title('Original')
    plt.subplot(1, 2, 2), plt.imshow(cv.cvtColor(imgBlur, cv.COLOR_BGR2RGB)), plt.title('Fundo borrado')

    plt.show()
    
    pass

if __name__== "__main__":
    main()