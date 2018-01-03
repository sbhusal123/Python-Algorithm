#see the documentation.
from sklearn.datasets import  *
import  pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt

boston = load_boston()

# format data
bos = pd.DataFrame(boston.data)
bos.columns = boston.feature_names
bos['Price'] = boston.target
# print(bos.head())

train_x = boston['data'][:500]
train_y = boston['target'][:500]




KNR = KNeighborsRegressor(1)
KNR.fit(train_x,train_y)


test = np.array(boston['data'][500])
test1 = test.reshape(1,-1)
print(bos.ix[500:])

print(KNR.predict(test1))
