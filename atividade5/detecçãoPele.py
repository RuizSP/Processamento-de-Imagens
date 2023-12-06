import numpy as np
import cv2

def skinDetection(image, hue, sat, value):
    # Converte a imagem para o espaço de cores HSV
    hsvimg = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define o intervalo de cores que correspondem à pele humana
    lower_skin = np.array([hue['min'], sat['min'], value['min']])
    upper_skin = np.array([hue['max'], sat['max'], value['max']])
    
    # Cria uma máscara para os pixels que estão dentro do intervalo de cores da pele
    skin_mask = cv2.inRange(hsvimg, lower_skin, upper_skin)
    
    # Aplica a máscara para isolar a região de pele
    skin_result = cv2.bitwise_and(image, image, mask=skin_mask)
    
    return skin_result

# Carregue a imagem
image = cv2.imread('exemplo.jpeg')

# Defina os intervalos de cor da pele (ajuste conforme necessário)
hue_range = {'min': 0, 'max': 20}
saturation_range = {'min': 30, 'max': 255}
value_range = {'min': 50, 'max': 255}

# Aplique a detecção de pele na imagem
skin_result = skinDetection(image, hue_range, saturation_range, value_range)

# Salve a nova imagem
cv2.imwrite('skin_detected.jpg', skin_result)

# Mostre a imagem original e a imagem resultante
cv2.imshow('Original Image', image)
cv2.imshow('Skin Detected Image', skin_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
