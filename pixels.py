import cv2


img = cv2.imread('images/lenna.png', cv2.IMREAD_COLOR)

# Acessando um pixel qualquer
pixel = img[30, 30]
print(pixel)
# Como a imagem eh colorida e nao referenciei um canal, o pixel terah 3 valores


img2 = cv2.imread('images/lenna.png', cv2.IMREAD_GRAYSCALE)

# Acessando um pixel qualquer
pixel2 = img2[30, 30]
print(pixel2)

# Como a imagem eh em tons de cinza, o pixel terah 1 valor
