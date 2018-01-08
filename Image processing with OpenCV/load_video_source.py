import cv2
import  numpy as np

cap = cv2.VideoCapture(0)
codec = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',codec , 20.0 , (640,480))
while True:
    #takes frames in infinite loop
    ret , frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # convert image frame to grayscale

    out.write(frame)
    #write the image frame on the file.

    #show both thw windows of different scales.
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)

    if( cv2.waitKey(1) & 0xFF == ord('q')):
        break
        #0xFF seems like keyboard input for 64 bit sys
        #go out of loop if pressed 'q'

cap.release()
# release the camera from the cv2 access
#so that it can be accessed
out.release()
#relase the video writer from the system
cv2.destroyAllWindows()


