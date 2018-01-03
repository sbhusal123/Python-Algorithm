import numpy as np

#array addition and substraction
a = np.array([2,5,3,8])
# print (a+5)

#array multiplication

p = np.array([2,6,1,2])
q = np.array([1,2,3,4])
# print(p*q)

#matrix multiplication

c = np.ones([3,3])
# print(c.dot([3,3,3]))

#computing sum,minimum,maximum
# print(a)
# print (np.sum(a)) #sum of all elements inside array
# print(np.min(a))
# print(np.max(a))
# print(np.argmin(a)) # place at which min occurs

#statistical computation
# print(a)
# print(np.mean(a))
# print(np.std(a)) #standard deviation

#flattening and reshaping
d = np.array([[1,2,3,],
             [4,5,6]])
# print(d)
# print(d.ravel())
e = d.ravel()
# print(e.reshape([3,2]))

#sorting
f = np.array([[5,3,1,2],
              [4,1,0,9]])
print(f)
# print(np.sort(f)) #only accross the row
print(np.sort(f,axis=0)) #accross the coloumn using axis
#axis takes 0 or 1. 0

# for more view documentation.

























