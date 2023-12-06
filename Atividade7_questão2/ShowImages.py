import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

def plotarImagens(imagens_originais, lista_imagens_comparacao, titulos_comparacao):
    num_imagens = len(imagens_originais)
    
    fig, axs = plt.subplots(num_imagens, 4, figsize=(15, 5 * num_imagens))
    
    for i in range(num_imagens):
        axs[i, 0].imshow(cv2.cvtColor(imagens_originais[i], cv2.COLOR_BGR2RGB))
        axs[i, 0].set_title('Imagem Original')
        axs[i, 0].axis('off')
        
        for j in range(1, 4):
            axs[i, j].imshow(cv2.cvtColor(lista_imagens_comparacao[j - 1][i], cv2.COLOR_BGR2RGB))
            axs[i, j].set_title(titulos_comparacao[j - 1])
            axs[i, j].axis('off')
    
    plt.show()