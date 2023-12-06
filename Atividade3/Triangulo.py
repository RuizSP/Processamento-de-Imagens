import cv2
import numpy as np

# Função para exibir uma imagem em uma janela
def openImage(imagem):
    cv2.imshow("Lontra", imagem)

# Função para desenhar um triângulo em uma imagem
def drawTriangle(imagem, points):
    pts = points
    # Desenha as bordas do triângulo na imagem
    cv2.polylines(imagem, [pts], True, (0,0,0))
    # Preenche o interior do triângulo com a cor preta
    cv2.fillPoly(imagem, pts=[points], color=(0,0,0))
    # Exibe a imagem com o triângulo desenhado
    cv2.imshow("Lontra com triangulo", imagem)
    # Salva a imagem com o triângulo em um arquivo
    cv2.imwrite("lontracomtriangulo.jpeg", imagem)

# Função para verificar se os pontos formam um triângulo
def isTriangle(points):
    # Calcula a área do triângulo utilizando a fórmula do determinante
    area = 0.5 * abs((points[0][0]*(points[1][1]-points[2][1]) +
                     points[1][0]*(points[2][1]-points[0][1]) +
                     points[2][0]*(points[0][1]-points[1][1])))
    # Retorna True se a área for maior que zero, indicando um triângulo válido
    return area > 0

# Função para verificar se os pontos estão dentro da área da imagem
def arePointsInsideImage(image, points):
    img_height, img_width = image.shape[:2]
    
    # Verifica cada ponto individualmente
    for point in points:
        x, y = point
        # Se algum ponto estiver fora da área da imagem, retorna False
        if x < 0 or x >= img_width or y < 0 or y >= img_height:
            return False
    # Se todos os pontos estiverem dentro da área da imagem, retorna True
    return True

# Função principal do programa
def main():
    caminhoImagem = "lontra.jpeg"
    imagem = cv2.imread(caminhoImagem)
    points = np.array([[20,20], [200,200], [200,20]])
    openImage(imagem)

    # Verificações para determinar se desenha o triângulo ou imprime mensagens
    if not isTriangle(points):
        print("Os pontos não formam um triângulo.")
    elif not arePointsInsideImage(imagem, points):
        print("Os pontos estão fora da área da imagem.")
    else:
        drawTriangle(imagem, points)

    cv2.waitKey(0)

if __name__ == "__main__":
    main()

