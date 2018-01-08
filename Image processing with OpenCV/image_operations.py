import  numpy as np
import cv2

img = cv2.imread('image.jpg',cv2.IMREAD_COLOR)

px = img[55,55]

print(px)
#BGR composn at that point

img[100:150, 100:150] = [255,255,255]
# from row 100 - 150 , column 100, 150  = COLOR

#defining the region of spaces
# ------------------------------------
my_region = img[37:700, 107:500]
# define region to be replaced
img[0:663,0:393] = my_region
# replace the region
# ------------------------------------

cv2.imshow('imaage',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
