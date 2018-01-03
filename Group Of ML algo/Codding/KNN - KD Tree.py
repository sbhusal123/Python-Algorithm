# KNN brute Force Searching


import numpy as np
from sklearn.neighbors import NearestNeighbors
import timeit

#data creation
X = np.random.random((1000, 3 ))
print(X)


#training
nn = NearestNeighbors(5,algorithm='kd_tree')
nn.fit(X)


# Testing
test = np.array([0.3,0.4,0.4])
test1 = test.reshape(1,-1)
print(nn.kneighbors(test1,5))



