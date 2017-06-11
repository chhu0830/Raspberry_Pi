#!/usr/bin/python3
import cv2
import sys
import config
from utils import surf

path = config.DIR['contours']
file1 = sys.argv[1]
file2 = sys.argv[2]

img1 = cv2.imread(path + file1, 0)
img2 = cv2.imread(path + file2, 0)

print(surf(img1, img2))
