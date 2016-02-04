import numpy as np
import cv2
 
im = cv2.imread('Tan9.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#print contours
cv2.drawContours(im, contours, -1, (0,255,0), 3)
cv2.imshow("Output", im)

cv2.waitKey(0)