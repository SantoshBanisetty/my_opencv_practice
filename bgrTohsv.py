import cv2
import numpy as np

blue = np.uint8([[[255,0,0]]])
green = np.uint8([[[0,255,0]]])
red = np.uint8([[[0,0,255]]])
yellow = np.uint8([[[0,255,255]]])

hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
hsv_yellow = cv2.cvtColor(yellow, cv2.COLOR_BGR2HSV)

print "Blue in HSV"
print hsv_blue
print "Green in HSV"
print hsv_green
print "Red in HSV"
print hsv_red
print "Yellow in HSV"
print hsv_yellow
