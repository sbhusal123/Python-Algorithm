import cv2
import numpy as anp
import matplotlib.pyplot as plt

#open cv - BGR
#matplotlib - RGB

img = cv2.imread('image.jpg',cv2.IMREAD_GRAYSCALE)
# Name of image and image scale colour
#for more view cv2 documentation

#display using cv2
cv2.imshow('Image',img)
# name of window and image variable
cv2.waitKey(0)
# wait for key to close
cv2.destroyAllWindows()


#display using matplotlib
plt.imshow(img , cmap='gray',interpolation='bicubic')
# to see the effect of interplolation remove and check effect.
plt.plot([50,100],[80,200],'r',linewidth = 5)
#plotting the point
plt.show()


#saving the image
# cv2.imwrite('file_name.ext',imaage_variable)