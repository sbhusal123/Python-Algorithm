# K neighbour + classifier
#nearest neighbour + vote for class
from sklearn.datasets import *
import  pandas as pd
import matplotlib.pyplot as plt
import  numpy as np
from sklearn.neighbors import KNeighborsClassifier

def displayImage(i): #i = numberth record
    #to display image
    plt.imshow(digit['images'][i],cmap='Greys_r')
    plt.show()

digit = load_digits() #load the dataset in variable
dig = pd.DataFrame(digit['data'][0:1700])
print(digit.keys())
#for training purpose use the first 1701 records

#traininng samples
train_x = digit['data'][:1700]
train_y = digit['target'][:1700]

#now train
KNN = KNeighborsClassifier(10) #how many nearest points
KNN.fit(train_x,train_y) #fit the train data for algo analysis


#testing phase

#order the data properly
test = np.array(digit['data'][1726])
test1 = test.reshape(1,-1) #1 row and possible colms
print(test)
print(test1)

#predict the result
print(KNN.predict(test1))
displayImage(1726)




