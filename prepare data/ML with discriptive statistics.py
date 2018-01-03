# basic statistical calculations in the pandas
import  pandas as pd
index = ['age','workclass','fnlwgt','education','education-num','marital-status','occupation',
         'relationship','race','sex','capital-gain','capital-loss'
         ,'hours-per-weeks','native country','class']

df = pd.read_csv("adult.data",names=index)
# names is equivalent to assigning the key to access the feature. or assigning the feature to the dataset

# print(df.dtypes) #datatype of each features

# print(df.describe()) #basic statistics of the data

# print(df.groupby('class').size()) #size of the class feature as per the basic classification.


print(df.corr(method='pearson')) #how the dataset are co-rrelated





