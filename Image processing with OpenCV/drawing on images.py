import numpy as np
import cv2

img = cv2.imread('image.jpg',cv2.IMREAD_COLOR)

cv2.line(img , (0,0), (150,150), (255,0,0))
#        variable, start, end, RGB composition

cv2.rectangle(img, (15,25),(200,150),(0,255,0),5)
#        variable , start , end, color, line width

pts = np.array([[10,5],[20,30],[70,20],[50,100]],np.int32)
# points in array , data type

pts = pts.reshape(-1,1,2)
#reshape the array #see documentation of reshape

cv2.polylines(img, [pts], False, (0,255,255),5)
# img = variable to apply
# True = connect the initial and final point
# color
#size


cv2.circle(img, (100,63),55, (0,255,0), 10)
# line width = -1 fill it in the circle

#writing on the image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img , 'Padam And Surya' ,(550,530),font,1 ,(200,250,255),1,cv2.LINE_AA)
# Var , Text , start ,font,  font-size , color , thickness of letters, Line

cv2.imshow('image',img)
#see documentation for image resizing

cv2.waitKey(0)
cv2.destroyAllWindows()