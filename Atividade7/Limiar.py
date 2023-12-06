import cv2 as cv
import numpy as np

def remover_linhas_letras(source):
    # Converter a imagem para escala de cinza
  
    gray = cv.cvtColor(source, cv.COLOR_BGR2GRAY)
  
    # Aplicar limiarização para binarizar a imagem
    #th = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV,3,30)
    _,th = cv.threshold(gray,20,255,cv.THRESH_BINARY)
    return th
    
def limiarizacaoOTSU(source):
    gray = cv.cvtColor(source, cv.COLOR_BGR2GRAY)
    _,th = cv.threshold(gray,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    return th
    
def limiarizacaoAdaptive(source):
    gray = cv.cvtColor(source, cv.COLOR_BGR2GRAY)
    th = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
    return th
    
def main():
    map1 = cv.imread("mapa1.jpg")
    map2 = cv.imread("mapa2.jpg")
    map3 = cv.imread("mapa3.jpg")
    cartaGetulho = cv.imread("carta_getulio.jpg")
    newCartaGG = limiarizacaoOTSU(cartaGetulho)
    
    cv.imshow("Carta original", cartaGetulho)
    cv.imshow("Original - Mapa 1", map1)
    cv.imshow("Original - Mapa 2", map2)
    cv.imshow("Original - Mapa 3", map3)

    mapa_sem_linhas_letras1 = remover_linhas_letras(map1)
    mapa_sem_linhas_letras2 = remover_linhas_letras(map2)
    mapa_sem_linhas_letras3 = remover_linhas_letras(map3)
    
    cv.imshow("carta getulho limiarizada", newCartaGG)

    cv.imshow("Mapa sem Linhas/Letras - Mapa 1", mapa_sem_linhas_letras1)
    cv.imshow("Mapa sem Linhas/Letras - Mapa 2", mapa_sem_linhas_letras2)
    cv.imshow("Mapa sem Linhas/Letras - Mapa 3", mapa_sem_linhas_letras3)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
