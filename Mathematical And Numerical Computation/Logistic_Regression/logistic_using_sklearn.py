from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt

def plot(data):
    for i in range(0,data.shape[0]):
        if data[i][2] == 0:
            plt.scatter(data[i][0],data[i][1],marker='^',c='b')
        else:
            plt.scatter(data[i][0], data[i][1], marker='o', c='r')


itr = 10000



logisticRegr = LogisticRegression(random_state=None,max_iter=itr,solver='lbfgs',fit_intercept=True)



data = np.array([[1,2,0],
                 [2,1,0],
                 [2,3,0],
                 [3,2,0],
                 [4,1,0],
                 [1,4,0],
                 [5,2,1],
                 [2,5,1],
                 [3,4,1],
                 [4,3,1],
                 [6,1,1],
                 [1,6,1],
                 [7,0,1],
                 [0,7,1],
                 [8,1,1],
                 [1,8,1]])


x = data[:,0:-1]

y = data[:,-1]




logisticRegr.fit(x,y)

x_intercept = -logisticRegr.intercept_/logisticRegr.coef_[0][0]
y_intercept = -logisticRegr.intercept_/logisticRegr.coef_[0][1]

print("X- intercept = "+str(x_intercept))
print("Y- intercept = "+str(y_intercept))


x = np.arange(-1,10,1)

y = (x_intercept*y_intercept-y_intercept*x)/x_intercept

plt.plot(x,y)



plot(data)
plt.show()