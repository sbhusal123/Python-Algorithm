#  documentation link
# http://scikit-learn.org/stable/modules/neighbors.html
from sklearn.datasets import *
import  pandas as pd
import  numpy as np
from sklearn.neighbors import NearestNeighbors

#prepare the data frame wih features
iris = load_iris()
ir = pd.DataFrame(iris.data)
ir.columns = iris.feature_names
ir['CLASS'] = iris.target
# print(ir.head())

#nearest neighbout searching algorithm

nn =  NearestNeighbors(5) #5 most nearest point
nn.fit(iris.data) #fit the data
print(ir.describe())
test = np.array([5.3,3,2,2.5]) #test data
test1 = test.reshape(1,-1) #1 row and any number of columns

print(nn.kneighbors(test1,5)) #print the nearest neighbout
#two set of arrays. 1st array is the distance from our test
#2nd array is the nearer points

print(ir.ix[[98,64,43,23,57]])
#describtion of the nearest neighbour points.
#3 classes are nearer to the train dataset for train.
#thus it is of class 1.