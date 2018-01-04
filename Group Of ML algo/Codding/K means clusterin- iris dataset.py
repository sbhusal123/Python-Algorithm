import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import art3d
from sklearn.datasets import load_iris
from sklearn.cluster  import KMeans

#load dataset
iris = load_iris()

X = iris['data']
df = pd.DataFrame(X)
df.columns = iris.feature_names
df['target'] = iris.target
print(df.head())

#algorithm

km = KMeans(n_clusters=3,max_iter=1000)
km.fit(X)
# print(km.cluster_centers_)
# print(km.labels_)
# some of the lables are misinterpreted

df['K mean predicted'] = km.labels_
# print(df.head(100))
print(iris.keys())


plt.show()










