import numpy as np
import cv2
 
#im = cv2.imread('test.png')
cap = cv2.VideoCapture(0)

#Check if the camera is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")
while True:
    ret, frame = cap.read()
    cv2.imshow("Input", frame) 
    imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,127,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #print contours
    cv2.drawContours(frame, contours, -1, (0,255,0), 2)
    cv2.imshow("Output", frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()