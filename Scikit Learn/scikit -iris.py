#iris data set is based on clasification while the boston database is based upon linear regression
from  sklearn.datasets import *
import  pandas as pd

iris = load_iris()
print(iris.keys())
ir = pd.DataFrame(iris.data)
# print(ir.head())  #head for first five data, takes parameter
ir.columns = iris.feature_names #adding the column feature at top
ir['CLASS'] = iris.target
# ir['CLASS_NAME'] = iris.target_names . Here error because cannot fit the data properly
print(ir.head(150))


