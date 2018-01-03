import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

data = np.array([[-1, -1, 'c1'],[-2, -1,'c1'],[-3, -2, 'c1'],[1, 0, 'c2']
                    ,[2, 1, 'c2'],[3, 2,'c2']])
query = [-2,5,-1,5] #our test data set

df =  pd.DataFrame(data)
df.columns = ['x','y','Category']


# caculating the distance
dis = []

for i in range(6):
    dis.append(
        math.sqrt(
        (float(df.ix[i]['x'])-query[1])**2 +
        (float(df.ix[i]['y']) - query[1])**2
    )  )

df['dis'] =dis; #assigning to the new row

print('---------- Data Frame ---------------------')
print(df)
print('------------------------------------------- \n \n ')


print('---------- Query Data ---------------------')
print(query)
print('-------------------------------------------')

#plott the point
for i in range(6):
    if(df.ix[i]['Category'] == 'c1'):
        plt.scatter(df.ix[i]['x'], df.ix[i]['y'], s = 150, c='r')
    else:
        plt.scatter(df.ix[i]['x'], df.ix[i]['y'], s=150, c='b')
    plt.scatter(query[0], query[1], s=200, c = 'Y')

plt.grid()
plt.show()