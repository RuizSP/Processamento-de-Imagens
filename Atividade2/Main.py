import cv2
import numpy as np

def openImage(imagem):
    cv2.imshow("Lontra", imagem)

    print ("Altura (height): %d pixels" % (imagem.shape[0]))
    print ("Largura (width): %d pixels" % (imagem.shape[1]))
    print ("Canais (channels): %d"      % (imagem.shape[2]))
    print("Tamanho em bytes: %d bytes" % (len(imagem.tobytes())))
    print("Tipo de dados da imagem: %s" % (imagem.dtype))

    #cv2.waitKey(0) 

def openVideo():
    # Abre o arquivo de vídeo 'Super Mario Bros. - O Filme 2023 1080p WEB-DL DUAL 5.1.mkv'
    video = cv2.VideoCapture('Super Mario Bros. - O Filme 2023 1080p WEB-DL DUAL 5.1.mkv')
    
    # Entra em um loop enquanto o vídeo estiver aberto
    while video.isOpened():
        # Lê um frame do vídeo
        ret, frame = video.read()

        # Verifica se o frame foi lido com sucesso
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # Exibe o frame em uma janela chamada 'frame'
        cv2.imshow('frame', frame)

        # Aguarda 1 milissegundo para verificar se a tecla 'q' foi pressionada
        if cv2.waitKey(1) == ord('q'):
            break

    # Libera os recursos do objeto de vídeo
    video.release()

    # Fecha todas as janelas abertas pelo OpenCV
    cv2.destroyAllWindows()

#def reColorImage(imagem, percent):
  #  scaleFactor = percent/100
  #  for i in range(len(imagem)):
    #    for j in range(len(imagem)):
     #       imagem[i][j] = imagem[i][j]*scaleFactor
   # cv2.imshow("Imagem", imagem)
   # cv2.waitKey(0) 

def rescaleImage(imagem, percent):
    scaleFactor = percent/100
    res = cv2.resize(imagem, dsize=(int(imagem.shape[0]* scaleFactor), int(imagem.shape[1]*scaleFactor)), interpolation=cv2.INTER_CUBIC)
    cv2.imshow('Imagem', res)

    print ("Altura (height): %d pixels" % (res.shape[0]))
    print ("Largura (width): %d pixels" % (res.shape[1]))

def createImage(altura, largura):
    newImg = np.zeros((altura, largura, 3), dtype=np.uint8)
    
    column = int(largura/3)
    for i in range(0, int(altura)):
        for j in range(0, column):
            newImg[i, j, 0] = 0
            newImg[i, j, 1] = 0  
            newImg[i, j, 2] = 255
    for i in range(0, int(altura)):
        for j in range(column, column*2):
            newImg[i, j, 0] = 0
            newImg[i, j, 1] = 255
            newImg[i, j, 2] = 0
    for i in range(0, int(altura)): 
        for j in range(column*2, largura):
            newImg[i, j, 0] = 255
            newImg[i, j, 1] = 0
            newImg[i, j, 2] = 0 

    cv2.imshow("New Image", newImg)
    cv2.imwrite("Imagem3.png", newImg)



def main():
    caminhoImagem = "lontra.jpeg"
    imagem = cv2.imread(caminhoImagem)

    openImage(imagem)
    rescaleImage(imagem, 200)
    createImage(300,600)
    openVideo()
    cv2.waitKey(0)

if __name__ == "__main__":
    main()
