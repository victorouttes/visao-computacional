import cv2


img = cv2.imread('images/lenna.png', cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

limiar = 50
valor_max = 255
th1, img_bw = cv2.threshold(img_gray, limiar, valor_max, cv2.THRESH_BINARY)

cv2.imwrite('images/limiarizacao/lenna_bw.png', img_bw)
