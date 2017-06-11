#!/usr/bin/python3
import cv2
import sys
import config
import numpy as np
from utils import contours


ori = config.DIR['test']
dst = config.DIR['contours']
filename = sys.argv[1]

img = cv2.imread(ori + filename, 0);  
img = contours(img)

cv2.imwrite(dst + filename, img)
cv2.imshow(filename, img)
cv2.waitKey(0)  
cv2.destroyAllWindows()

