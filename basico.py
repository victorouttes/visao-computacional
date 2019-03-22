import cv2

# Load an color image in grayscale
img = cv2.imread('images/lenna.png', 0)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
