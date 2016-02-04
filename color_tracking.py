import cv2
import numpy as np

# Capture the input frame from webcam
def get_frame(cap, scaling_factor):
    # Capture the frame from video capture object
    ret, frame = cap.read()

    # Resize the input frame
    frame = cv2.resize(frame, None, fx=scaling_factor,
            fy=scaling_factor, interpolation=cv2.INTER_AREA)

    return frame

if __name__=='__main__':
    cap = cv2.VideoCapture(0)
    scaling_factor = 0.5

    # Iterate until the user presses ESC key
    while True:
        frame = get_frame(cap, scaling_factor)

        # Convert the HSV colorspace
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define 'blue' range in HSV colorspace
        b_lower = np.array([100,100,100])
        b_upper = np.array([140,255,255])

        # Define 'green' range in HSV colorspace
        g_lower = np.array([40,100,100])
        g_upper = np.array([95,255,255])

        # Define 'red' range in HSV colorspace
        r_lower = np.array([0,100,100])
        r_upper = np.array([20,255,255])

        # Define 'yellow' range in HSV colorspace
        y_lower = np.array([20,100,100])
        y_upper = np.array([40,255,255])


        # Threshold the HSV image to get only blue color
        b_mask = cv2.inRange(hsv, b_lower, b_upper)

        # Threshold the HSV image to get only green color
        g_mask = cv2.inRange(hsv, g_lower, g_upper)

        # Threshold the HSV image to get only red color
        r_mask = cv2.inRange(hsv, r_lower, r_upper)

        # Threshold the HSV image to get only yellow color
        y_mask = cv2.inRange(hsv, y_lower, y_upper)

        # Bitwise-AND mask and original image
        b_res = cv2.bitwise_and(frame, frame, mask=b_mask)
        b_res = cv2.medianBlur(b_res, 5)

        # Bitwise-AND mask and original image
        g_res = cv2.bitwise_and(frame, frame, mask=g_mask)
        g_res = cv2.medianBlur(g_res, 5)

        # Bitwise-AND mask and original image
        r_res = cv2.bitwise_and(frame, frame, mask=r_mask)
        r_res = cv2.medianBlur(r_res, 5)

        # Bitwise-AND mask and original image
        y_res = cv2.bitwise_and(frame, frame, mask=y_mask)
        y_res = cv2.medianBlur(y_res, 5)

        cv2.imshow('Original image', frame)
        cv2.imshow('Blue Color Detector', b_res)
        cv2.imshow('Green Color Detector', g_res)
        cv2.imshow('Red Color Detector', r_res)
        cv2.imshow('Yellow Color Detector', y_res)

        # Check if the user pressed ESC key
        c = cv2.waitKey(5)
        if c == 27:
            break

    cv2.destroyAllWindows()