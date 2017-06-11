import cv2
import numpy as np

def contours(img):
    kernel = np.ones((2, 2),np.uint8)
    erosion = cv2.erode(img, kernel, iterations = 5)

    thresh = 100
    edges = cv2.Canny(erosion, thresh, thresh*2)
    _, contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    black = np.zeros(img.shape, img.dtype)
    cv2.drawContours(black, contours, -1, (255,255,255), 3)

    return black

def surf(img1, img2):
    img2 = cv2.resize(img2, img1.shape[::-1])
    surf = cv2.xfeatures2d.SURF_create(6400)
    kp1, des1 = surf.detectAndCompute(img1, None)
    kp2, des2 = surf.detectAndCompute(img2, None)

    matched = []
    bf = cv2.BFMatcher()

    matches1 = bf.knnMatch(des1, des2, k=2)
    for m, n in matches1:
        if m.distance < 0.8 * n.distance:
            matched.append([m])

    matches2 = bf.knnMatch(des2, des1, k=2)
    for m, n in matches2:
        if m.distance < 0.8 * n.distance:
            matched.append([m])

    '''
    img1 = cv2.drawKeypoints(img1, kp1, None, (255, 0, 0), 4)
    img2 = cv2.drawKeypoints(img2, kp2, None, (255, 0, 0), 4)
    cv2.imshow(file1, img1)
    cv2.imshow(file2, img2)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()
    '''
    return len(matched) / (len(matches1) + len(matches2))
