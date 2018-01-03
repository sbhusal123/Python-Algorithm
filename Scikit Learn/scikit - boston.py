from sklearn.datasets import  *
import pandas as pd

boston = load_boston()
# print(boston.keys()) all data,feature_names,target are keys
bos = pd.DataFrame(boston.data) #loadinng the data in pandas data frame
bos.columns = boston.feature_names #1st column is set as features names
bos['PRICE'] = boston.target #our target is finding the price
print(bos.head) #now print the dataframe
