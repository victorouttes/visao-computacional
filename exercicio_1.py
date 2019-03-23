import cv2


# Ler a imagem e adicionar uns quadrados de lado 30, como nos slides
img = cv2.imread('images/fac-ibratec.png', cv2.IMREAD_COLOR)

img[0:30, 0:30] = [255, 0, 0]
img[30:60, 30:60] = [0, 255, 0]
img[60:90, 60:90] = [0, 0, 255]
img[0:45, 60:105] = [20, 102, 204]

cv2.imwrite('images/exercicio_1/resultado.png', img)
