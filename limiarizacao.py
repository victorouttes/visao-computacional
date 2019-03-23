import cv2


img = cv2.imread('images/lenna.png', cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

threshold_default = 125
valor_max = 255
th1, img_bw = cv2.threshold(img_gray, threshold_default, valor_max, cv2.THRESH_OTSU)
print('Limiar = ' + str(th1))

cv2.imwrite('images/limiarizacao/lenna_bw.png', img_bw)
