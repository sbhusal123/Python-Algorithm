#see scikit learn documentation for more
# http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.DistanceMetric.html

from sklearn.neighbors import DistanceMetric

X = ([[1,1],[2,2],[2,4]])

'''
Matrix computation
X[0,0] = sqrt(1-1)**2 + (1-1)**2
X[0,1] = sqrt(2-1)**2 +(2-1)**2
X[0,2] = sqrt(2-1)**2 + (4-1)**2
X[1,0] = sqrt(2-1)**2 + (4-1)**2
X[1,1] = sqrt(2-2)**2 + (2-2)**2
X[1,3] = sqrt(2-2)**2 + (2-4)**2

forst calculates the X[i]*X[j] then operates 
on euclidean distance measure
'''

eu = DistanceMetric.get_metric('euclidean')
print(eu.pairwise(X))



