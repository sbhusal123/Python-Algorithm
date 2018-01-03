from sklearn.datasets import *
import pylab as pl #used in visualizing the matrix dataset

index = 113
digits = load_digits()
print(digits.images[index])
print(digits.target[index])
pl.gray() #using the color schema
pl.matshow(digits.images[index]) #put the image in frame.
pl.show()






