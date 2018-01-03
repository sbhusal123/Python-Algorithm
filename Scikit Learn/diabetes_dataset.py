from sklearn.datasets import *
import pandas as pd
diabetes = load_diabetes()
print(diabetes.keys())

di = pd.DataFrame(diabetes.data)
di.columns = diabetes.feature_names;
print(di)
print(diabetes.DESCR)
