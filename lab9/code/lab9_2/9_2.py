import cv2
import numpy as np
img = cv2.imread('nctu.JPG')
img_logo = cv2.imread('NCTU_LOGO.png')

img = img[150:370, 0:]

img_rows, img_cols = img.shape[:2]

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_logo = cv2.cvtColor(img_logo, cv2.COLOR_BGR2GRAY)

img_logo = cv2.resize(img_logo, 
                      (img_rows, img_rows),
                      3)

matrix = cv2.getRotationMatrix2D((img_rows/2,
                                  img_rows/2),
                                 90,
                                 1)
img_logo = cv2.warpAffine(img_logo,
                          matrix,
                          (img_cols, img_rows))

print(img.shape)
print(img_logo.shape)

dst = cv2.add(img, img_logo)

cv2.imshow("Image_g", dst) 
cv2.imwrite('merge.jpg', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()



