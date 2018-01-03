#unsupervised way of learning
import  numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#generate random data for cluster 1 ie left one
X = -2 + np.random.rand(100,2)
#generate random num - 2
#rand  data between 0 and 1
#size is 100 by 2

#generate random data for cluster 2
X1 = 1+ 2 * np.random.rand(50,2)


#mixing the two randomly generated numbers ie right one
X[50:100,:] = X1
# last 50-100 row element belong to X1
# total element in the X is 200 as size is (100,2)
#100 row and 2 columns

# print(X)
#
# print(X.size)
# print(X.shape)

# print(X[:,0]) prints the first column


#algorithm implemenation
Kmean =  KMeans(n_clusters = 2); # number of clusters is 2
Kmean.fit(X) # fit the data for algo analysis
center  = Kmean.cluster_centers_
#find the center and store in variable center
print(center)





#testing
test = np.array([4,4])
test1 =  test.reshape(1,-1)
print(Kmean.predict(test1))
print(Kmean.labels_) #prints the labels associated with the cluster


#plot the data
#plot points
plt.scatter(X[:,0], X[:,1], s=50, c= 'b')
#plot the center points
plt.scatter(center[0,0] , center[0,1], s = 100 , c= 'r')
plt.scatter(center[1,0] , center[1,1], s = 100 , c= 'g')
# show plot
plt.show()

#how is the data plotted?
'''
first column is plotted by X[:,0] refres to X
second column is plotted by X[,:1] refres to Y
plot scatter consists of 100 points each (x,y)
'''