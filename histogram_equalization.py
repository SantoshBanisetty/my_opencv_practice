import cv2
import numpy as np

image = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)
histEq = cv2.equalizeHist(image)

cv2.imshow("Input", image)
cv2.imshow("Histogram Equalized", histEq)

cv2.waitKey(0)