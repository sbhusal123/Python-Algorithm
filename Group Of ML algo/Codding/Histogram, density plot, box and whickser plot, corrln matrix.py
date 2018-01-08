import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

# #preparing own data sets
# data = np.array([[6,148,72,35,0,33.6,0.627,50,1],
#                  [1,85,66,29,0,26.6,0.351,31,0],
#                  [8,183,64,0,0,23.3,0.627,32,1],
#                  [1,89,66,23,94,28.1,0.167,21,0],
#                  [0,137,40,35,168,43.1,2.283,33,1]
#                  ])
# ind = ['preg','plas','pres','skin','test','mass','pedi','age','class']
# df = pd.DataFrame(data)
# df.columns = ind
# print(df)
#
# #histogram
# df.hist()
# plt.show()
#
# #density plot



iris = load_iris()
df = pd.DataFrame(iris.data)
df.columns = iris.feature_names
# df.hist()
# basically the histogram show how many datas are available


#density plot
df.plot(kind='density',subplots = True,layout=(2,2),sharex= False)
# subplots seprates the plots as per the features
#layout places 2 graph per column as per data
plt.show()
