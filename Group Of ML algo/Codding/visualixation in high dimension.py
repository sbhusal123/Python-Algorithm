from pandas.plotting import parallel_coordinates
from sklearn.datasets import load_iris
import pandas as pd


#visualize in 4 dimension
def mapTarget(target):
    if target == 0:
        return 'setosa'
    if target == 1:
        return 'versicolor'
    if target == 2 :
        return 'virgincia'



ir = load_iris()
df = pd.DataFrame(ir['data'], columns = ir['feature_names'])
df['target'] = ir['target']
df['target_name'] = list(map(mapTarget,df['target']))
print(df)



#apply the parallel coordinates: this code in shell 2
parallel_coordinates(df[:50],'target_name')


