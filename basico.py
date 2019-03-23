import cv2


img = cv2.imread('images/lenna.png', cv2.IMREAD_COLOR)

# Mostra a imagem
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Estrutura da imagem
print(img.shape)
# Quantidade de pixels da imagem
print(img.size)
# Tipo do objeto
print(img.dtype)


