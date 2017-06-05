import cv2  
import numpy as np    
   
 
img = cv2.imread("cat_sa.jpg")  

result = img
median2 = cv2.medianBlur(img, 7)
  
cv2.imshow("Salt", result)  
cv2.imshow("Median", median2)  

cv2.imwrite('median.jpg', median2)
  
cv2.waitKey(0)
