import cv2
import numpy as np

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')

add = img1 + img2
# added images


add_pixels = cv2.add(img2,img1)
# add the pixel value of images together

weighted = cv2.addWeighted(img1, 0.4 , img2, 0.6 , 0)
#  image1 , img1-weight, img2 , img2-weight , gama

# weight is actualy opaqueness


cv2.imshow('Weighted',weighted)

cv2.imshow('added',add)

cv2.imshow('Pixel Addition', add_pixels)
# show added images

cv2.imshow('image1',img1)
cv2.imshow('image2',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()