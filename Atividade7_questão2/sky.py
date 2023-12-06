import cv2
import os
import numpy as np
import ShowImages as SI

def aplicarLimiar(img):
   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   _,binary =  cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
   _,OTSU = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
   adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 41, 2)
   return binary, OTSU, adaptive

def acuracy(img, ground):
    
    value = np.mean(np.equal(img, ground))
    return value 

def calcularAcuracyMedia(imgs, ground):
    lst = []
    for i in range(len(imgs)):
        lst.append(acuracy(imgs[i], ground[i]))
    return (sum(lst)/len(lst)) * 100

def carregarImagens(caminho):
    # Lista para armazenar as imagens carregadas
    imagens = []
    # Verifique se a pasta existe
    if os.path.exists(caminho):
        # Percorre todos os arquivos na pasta e ordene-os alfabeticamente
        arquivos = sorted(os.listdir(caminho))
        print(len(arquivos))
        for nome_arquivo in arquivos:
            # Verifique se o arquivo é uma imagem (você pode adicionar mais extensões se necessário)
            if nome_arquivo.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.pgm')):
                # Construa o caminho completo para o arquivo
                caminho_completo = os.path.join(caminho, nome_arquivo)
                
                
                
                # Carregue a imagem usando o OpenCV
                imagem = cv2.imread(caminho_completo)
                if nome_arquivo.endswith('.pgm'):
                   imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
                   imagem = cv2.multiply(imagem, 255)
                
                # Verifique se a imagem foi carregada com sucesso
                if imagem is not None:
                    imagens.append(imagem)
            else:
                print(f"Arquivo {nome_arquivo} não é uma imagem suportada.")

        if len(imagens) > 0:
            print(f"{len(imagens)} imagens carregadas com sucesso.")
        else:
            print("Nenhuma imagem foi encontrada na pasta.")
    else:
        print(f"A pasta {caminho} não existe.")
    return imagens

    

def aplicarLimiarEmLista(imagens):
    blst= []
    olst=[]
    alst=[]
    for i in range(len(imagens)):
        b,o,a = aplicarLimiar(imagens[i])
        blst.append(b)
        olst.append(o)
        alst.append(a)
    return blst, olst, alst

def main():


    pasta_atual = os.getcwd()
    
    # Pasta contendo as imagens (substitua 'data' pelo nome da sua pasta)
    caminho = os.path.join(pasta_atual, 'data')
    pasta_ground = os.path.join(pasta_atual, 'groundtruth')

    lstImagens = carregarImagens(caminho)
    lstGround = carregarImagens(pasta_ground)
    cv2.imshow("ground", lstGround[3])  


    listaBinary, listaOTSU,listaAdaptive = aplicarLimiarEmLista(lstImagens)
    cv2.imshow("Original", lstImagens[6])
    cv2.imshow("Binary1", listaBinary[6])
    cv2.imshow("OTSU1", listaOTSU[6])
    cv2.imshow("adaptive1", listaAdaptive[6])
   


    mediaBinary= calcularAcuracyMedia(listaBinary[4:], lstGround[4:])
    mediaOTSU = calcularAcuracyMedia(listaOTSU[4:], lstGround[4:])
    mediaAdaptive = calcularAcuracyMedia(listaAdaptive[4:], lstGround[4:])

    medias = [mediaBinary, mediaOTSU, mediaAdaptive]
    print(medias)
    
    if max(medias) == medias[0]:
        print(f"Binary Threshold teve a melhor média de acurácia: {medias[0]}%")
    if max(medias) == medias[1]:
        print(f"OTSU Threshold teve a melhor média de acurácia: {medias[1]}%")
    if max(medias) == medias[2]:
        print(f"Adaptive Threshold teve a melhor média de acurácia: {medias[2]}%")


    cv2.waitKey(0)
if __name__ == "__main__":
    main()
