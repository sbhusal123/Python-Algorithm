# https://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html ---> documentation
# masking?
# bitwise operations.
import cv2
import numpy as np

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainlogo.png')

rows, cols , chanels = img2.shape
# rows in image pixels
# colms in image pixels
# channel of color
# 126 by 126 image

roi = img1[0:rows,0:cols]
'''copy the same dimension as of the 
image2 from image1
'''

img2gray = cv2.cvtColor(img2 , cv2.COLOR_BGR2GRAY)
# convert the color of image from BGR to Gray

ret, mask = cv2.threshold(img2gray , 220, 255, cv2.THRESH_BINARY_INV)
# mask is threshold
# imagevar , thres-value , max value , type of threshold

'''
What is threshold?
-> If the pixel value is above 220  -> cont to 255(black)
-> If it's below 220 convert to black(0)
-> To understand threshold compare images img2 and mask
'''
cv2.imshow('mask',mask)
# cv2.imshow('Python Logo',img2) -> to understand threshold

mask_inv = cv2.bitwise_not(mask)
cv2.imshow('mask_inv',mask_inv)
# color shift back -> white , white -> black

img1_bg = cv2.bitwise_and(roi, roi ,mask=mask_inv)
cv2.imshow('img1_bg',img1_bg)

img2_fg = cv2.bitwise_and(img2,img2,mask=mask)
# need documentation
'''
from documentation
cv2.bitwise_and(src1, src2[, dst[, mask]]) 
Parameters:	
src1 – first input array or a scalar.
src2 – second input array or a scalar.
src – single input array.
value – scalar value.
dst – output array that has the same size and type as the input arrays.
mask –  optional operation mask, 
        8-bit single channel array, that specifies elements 
        of the output array to be changed.
        
What is masking?
->Masking involves setting the pixel values in an image to zero, or some other "background" value. ... 
  A mask image is simply an image where some of 
  the pixel intensity values are zero, and others are non-zero.
'''
cv2.imshow('img2_fg',img2_fg)


dst = cv2.add(img1_bg,img2_fg)
cv2.imshow('dst',dst)

img1[0:rows,0:cols] = dst

# cv2.imshow('res',img1)



# cv2.imshow(mask_inv)
# img1_bg = cv2.bitwise_and()
# logical operator

cv2.waitKey(0)
cv2.destroyAllWindows()