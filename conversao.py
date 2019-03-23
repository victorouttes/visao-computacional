import cv2


img = cv2.imread('images/lenna.png', cv2.IMREAD_COLOR)
# Converte para tons de cinza
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
