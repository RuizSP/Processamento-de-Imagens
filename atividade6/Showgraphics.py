import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt



def plotGraphics2(img1, img2, hist_channels1, hist_channels2):
	# Subplot para a imagem 1
    plt.subplot(2, 2, 1)
    plt.imshow(cv.cvtColor(img1, cv.COLOR_BGR2RGB))
    plt.title('Imagem Original')
    
      # Subplot para a imagem 2
    plt.subplot(2, 2, 2)
    plt.imshow(cv.cvtColor(img2, cv.COLOR_BGR2RGB))
    plt.title('Imagem Equalizada')
    
     # Subplot para hist_chanels1
    plt.subplot(2, 2, 3)
    plt.title('Histograma - Original')
    plt.xlabel('Intensidade')
    plt.ylabel('Número de Pixels')

    for i, color in enumerate(('b', 'g', 'r')):
        plt.plot(hist_channels1[i], color=color, label=f'Canal {color.upper()}')

    plt.xlim([0, 256])
    plt.legend()

    plt.tight_layout()
    
        # Subplot para hist_chanels2
    plt.subplot(2, 2, 4)
    plt.title('Histograma - equalizado')
    plt.xlabel('Intensidade')
    plt.ylabel('Número de Pixels')

    for i, color in enumerate(('b', 'g', 'r')):
        plt.plot(hist_channels2[i], color=color, label=f'Canal {color.upper()}')

    plt.xlim([0, 256])
    plt.legend()

    plt.tight_layout()
    plt.show()
    

def plotGraphics(img1, img2, hist1, hist_channels):
    plt.figure(figsize=(12, 6))

    # Subplot para a imagem colorida
    plt.subplot(2, 3, 1)
    plt.imshow(cv.cvtColor(img1, cv.COLOR_BGR2RGB))
    plt.title('Imagem Colorida')

    # Subplot para a imagem em tons de cinza
    plt.subplot(2, 3, 2)
    plt.imshow(cv.cvtColor(img2, cv.COLOR_BGR2RGB), cmap='gray')
    plt.title('Imagem em Tons de Cinza')

    # Subplot para o histograma em tons de cinza
    plt.subplot(2, 3, 3)
    plt.title('Histograma - Tons de Cinza')
    plt.xlabel('Intensidade')
    plt.ylabel('Número de Pixels')
    plt.plot(hist1)
    plt.xlim([0, 256])

    # Subplot para o histograma dos canais de cores (vermelho, verde e azul)
    plt.subplot(2, 1, 2)
    plt.title('Histograma - Canais de Cores')
    plt.xlabel('Intensidade')
    plt.ylabel('Número de Pixels')

    for i, color in enumerate(('b', 'g', 'r')):
        plt.plot(hist_channels[i], color=color, label=f'Canal {color.upper()}')

    plt.xlim([0, 256])
    plt.legend()

    plt.tight_layout()
    plt.show()
