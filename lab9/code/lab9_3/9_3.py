import cv2
import numpy as np

img_origin = cv2.imread('building.jpg',0);  
img = img_origin

edge_f = cv2.Canny(img, 100, 200)
edge_f = cv2.bitwise_not(edge_f)

cv2.imshow('edge_f',edge_f)
cv2.imwrite('edge.jpg', edge_f)

x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
y = cv2.Sobel(img, cv2.CV_16S, 0, 1)


absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)

sobel_r = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
sobel_r = cv2.bitwise_not(sobel_r)

cv2.imshow('Sobel', sobel_r)  
cv2.imwrite('sobel.jpg', sobel_r)

cv2.waitKey(0)  
cv2.destroyAllWindows()



 
  
  

