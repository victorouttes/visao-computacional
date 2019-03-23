import cv2


img = cv2.imread('images/lenna.png', cv2.IMREAD_COLOR)

# Pegando os canais de cor separadamente
b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]

# Salva os 3 canais de cor em imagens diferentes
cv2.imwrite('images/canais/lenna-B.png', b)
cv2.imwrite('images/canais/lenna-G.png', g)
cv2.imwrite('images/canais/lenna-R.png', r)
