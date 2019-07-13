import numpy as np
from sklearn.decomposition import PCA


x = np.array([[1,2],
              [3,4]])

pca = PCA(n_components=1)

pca.fit(x)


print(pca.transform(x))











