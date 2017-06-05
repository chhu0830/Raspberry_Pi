import cv2
import numpy as np

path = '../data/test/'
filename = 'back.jpg'

img = cv2.imread(path + filename);  
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.ones((2, 2),np.uint8)
erosion = cv2.erode(gray, kernel, iterations = 5)

thresh = 100
edges = cv2.Canny(erosion, thresh, thresh*2)
_, contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

white = 255 * np.ones(img.shape, img.dtype)
cv2.drawContours(white, contours, -1, (0,0,0), 3)

cv2.imshow(filename, img)
cv2.imshow('contours', white)  

cv2.waitKey(0)  
cv2.destroyAllWindows()

