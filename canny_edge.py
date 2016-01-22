import cv2
import numpy as np

image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original", image)
canny = cv2.Canny(image, 50, 240)
cv2.imshow("Canny edge", canny)
cv2.waitKey(0)