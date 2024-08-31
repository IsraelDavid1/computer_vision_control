import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# range of yellow color

yellow_lower = np.array([22, 93, 0])
yellow_upper = np.array([45, 255, 255])

while True:
    ret, frame = cap.read()
    #give the frame high saturation
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, yellow_lower, yellow_upper)
    cv2.imshow('frame', frame)
    # the mask is to detect the color specified in range
    cv2.imshow('mask', mask)
    if cv2.waitKey(10)  == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()