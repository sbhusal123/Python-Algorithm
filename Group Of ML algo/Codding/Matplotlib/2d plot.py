import numpy as np
import matplotlib.pyplot as plt

#create numpy array
x = np.array([[1,2,],[3,4],[4,5],[5,6],[7,8]])
# print(x)
# print(x[:,0])
# print(x[:,1])
plt.scatter(x[:,0],x[:,1],s = 5 , c = 'r')
plt.xlabel('X - axis')
plt.ylabel('Y- axis')
plt.show()


