from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time

#Define the Lower and upper boundaries of the "green" ball in the HSV color space
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)

#Set up buffer size for tracking the ball
buffer_size = 64
pts = deque(maxlen=buffer_size)

#Start the webcam 
vs = VideoStream(src=0).start()  # Use 0 for the default webcam
time.sleep(2.0)  # Allow the camera to warm up

#Start
while True:
    #current frame
    frame = vs.read()

    #Resize the frame for faster processing
    frame = imutils.resize(frame, width=600)

    #Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Create a mask for the green color
    mask = cv2.inRange(hsv, greenLower, greenUpper)

    #Perform a series of dilations and erosions to remove small blobs in the mask
    mask = cv2.dilate(mask, None, iterations=2)
    mask = cv2.erode(mask, None, iterations=1)

    #Find contours in the mask
    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    center = None

    #If at least one contour was found
    if len(contours) > 0:
        #Sort the contours by area and take the largest one
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:1]

        #Get the bounding box for the largest contour
        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            #Draw the bounding box on the frame
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            center = (x + w // 2, y + h // 2)

            #Draw the center of the ball
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

    #Update the points deque with the new center of the ball
    pts.appendleft(center)

    #Loop over the tracked points and draw them on the frame
    for i in range(1, len(pts)):
        if pts[i - 1] is None or pts[i] is None:
            continue
        thickness = int(np.sqrt(buffer_size / float(i + 1)) * 2.5)
        cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)

    #Display the frame
    cv2.imshow("Ball Tracking", frame)

    #Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

#release the video stream and close any open windows
vs.stop()  #Stop the video stream
cv2.destroyAllWindows()  #Close all windows
