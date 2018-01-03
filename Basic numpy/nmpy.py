# numpy consists of basic numbering library and maths library.
from timeit import timeit

import  numpy as np
import time
from builtins import print

b = np.array([[3,5,7],[1,6,3]]) #matrix
a = np.array([1,2,3,4])
# print (a)
# print (a.shape)

c = np.array([[1,2,3,4,5],
              [2,5,6]])
# print (c)
c = np.arange(3,20,4)


d = np.linspace(0,4,3)
# print(d)

e = np.ones([2,2])
# print (e)
e = 7*e
# print(e)

#random numbers
g = np.random.rand(3) #uniform distbibuted way between 0 and 1
# print(g)

h = np.random.randn(4)
# print(h)

#basic data types.
c = np.arange(1,20,4)
# print(c)
# print(c.dtype)

k = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(k)
# print(k[:,1]) # : here
# print(k[1,:])


