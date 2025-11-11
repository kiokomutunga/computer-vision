import cv2
import numpy as np

###convrting gray scale

img = cv2.imread("C:/Users/kioko/Desktop/computer vision/resources/lyn.png")   
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print("output", img.shape)
print("image grayshape", img_gray.shape)

#show the images
cv2.imshow("Original Image", img)
cv2.imshow("Gray Image", img_gray)

cv2.waitKey(0)