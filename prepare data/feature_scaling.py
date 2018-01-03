#scaling down to the poper range of value

import numpy as np
from sklearn import preprocessing


#minimax scalar --> scalling to ceratain range.
# X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
# X_scaled = X_std * (max - min) + min
print('----Min Max Scaling--------')

x = np.array([[1,2,3],[4,5,6],[7,8,9]])
# x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]) test it
print(x)
minmax =  preprocessing.MinMaxScaler(feature_range=(0,1))

print(minmax.fit(x).transform(x))

print('---------------------------')


'''
First Feature
min = 1 
min = 7
x_std[0] = (1-1)/(7-1)
X_std[4] = (4-1) /(7-1)
x_std[7] = (7-1)/(7-1)
'''

print('---------- Standard Scaing -----------')
# Standard Scalar
standard = preprocessing.StandardScaler().fit(x);
print(standard.transform(x))

'''
x_std[0] = (1-4)/np.std(x[:,0]
'''
print('--------------------------------------')

#Binarizer scaling
'''
Giving the threshold for the each data. eg in the Neural net 
'''
print('------------ Binarizer --------------------')
print(preprocessing.Binarizer(3.0).fit(x).transform(x))
print('-------------------------------------------')


#Normalize
'''
x0 = 1
norm0 = math.sqrt(1+4+9)
x0/norm0
'''
print('--------- Normalize ------------')
print(preprocessing.Normalizer().fit(x).transform(x))

print('--------------------------------')


