import cv2


def media_global(hist):
    mg = 0
    for i in range(len(hist)):
        mg += i * hist[i]
    return mg


def media_classes(hist, limiar):
    p1, p2 = prob_classes(hist, limiar)
    m1 = 0
    for i in range(0, limiar+1):
        m1 += i * hist[i]

    m2 = 0
    for i in range(limiar+1, len(hist)):
        m2 += i * hist[i]

    med1 = 0
    med2 = 0
    if p1 > 0:
        med1 = m1/p1
    if p2 > 0:
        med2 = m2/p2
    return med1, med2


def prob_classes(hist, limiar):
    p1 = 0
    for i in range(0, limiar+1):
        p1 += hist[i]

    p2 = 0
    for i in range(limiar+1, len(hist)):
        p2 += hist[i]
    return p1, p2


def var_max(p1, m1, p2, m2, mg):
    return p1 * (m1 - mg)**2 + p2 * (m2 - mg)**2


img = cv2.imread('images/H01.png', cv2.IMREAD_GRAYSCALE)
qtd_pixels = img.size
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
hist_normalizado = [h[0]/qtd_pixels for h in hist]
mg = media_global(hist_normalizado)

limiar_best = 0
variancia_best = 0

for limiar in range(0, 256):
    m1, m2 = media_classes(hist_normalizado, limiar)
    p1, p2 = prob_classes(hist_normalizado, limiar)
    variancia = var_max(p1, m1, p2, m2, mg)
    if variancia > variancia_best:
        variancia_best = variancia
        limiar_best = limiar

print('OTSU: ' + str(limiar_best))
th1, img_bw = cv2.threshold(img, limiar_best, 255, cv2.THRESH_BINARY)
cv2.imwrite('images/limiarizacao/otsu.png', img_bw)
