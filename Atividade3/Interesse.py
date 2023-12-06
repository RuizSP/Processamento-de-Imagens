import cv2 as cv
import numpy as np




def crop(imagem, x_bola, y_bola, largura_bola, altura_bola):
	#utiliza recorte de fatias do numpy, y_bola = valor inicial em y, y_bola+altura_bola = valor final em y, o mesmo vale para x
	# y_bola+altura_bola: se eu tenho a posicao inicial e a altura da bola, a posicao finala é dada pela soma das duas (o mesmo vale em x) 
	cropedImage = imagem[y_bola:y_bola+altura_bola, x_bola:x_bola + largura_bola]
	return cropedImage


def paste(src, dst, x, y):
	newImage = src
	if x>=0 and y>=0:
		for i in range(0, dst.shape[0]):
			for j in range(0, dst.shape[1]):
				if(i+y < newImage.shape[0] and j+x < newImage.shape[1]): #verifica se a posição ainda está dentro do tamanho da imagem original
					newImage[i+y,j+x] = dst[i][j]
	else:
		print("X e Y devem ser valores maiores que 0")
	return newImage
			
def main():
	x_bola = 336
	y_bola = 287
	largura_bola = 55
	altura_bola = 163
	
	
	caminhoImagem = "messi.jpg"
	imagem = cv.imread(caminhoImagem)
	cv.imshow("Messi", imagem)
	ballImg = crop(imagem, x_bola, y_bola, largura_bola, altura_bola)
	newImage = paste(imagem, ballImg, 92, 279)
	cv.imshow("2 bola", newImage)
	cv.imwrite("2bola.png", newImage)
	cv.waitKey(0)
	
	

if __name__ == "__main__":
	main()
