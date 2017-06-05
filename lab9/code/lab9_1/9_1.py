import cv2
import numpy as np

img = cv2.imread('2cat.jpg')

#divde
h, w, c = img.shape
black = img[0:h, 0:int(w/2)]
white = img[0:h, int(w/2):w]

#turn into gray
white = cv2.cvtColor(white, cv2.COLOR_BGR2GRAY)
cv2.imwrite('white_cat.png',
            white,
            [int(cv2.IMWRITE_PNG_COMPRESSION)])
cv2.imwrite('black_cat.jpg',
            black,
            [int(cv2.IMWRITE_JPEG_QUALITY), 5])

cv2.imshow('Normal', img) 

cv2.waitKey (0)
cv2.destroyAllWindows()



