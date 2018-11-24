import numpy as np
import matplotlib.pyplot as plt
#caution!---- This is not so good idea for regression ------


def featureScaling(data):
    std = np.std(data)
    mean = np.mean(data)

    data = (data-mean)/std

    return data




def cost(data,theta):
    inp_feature = data[:,0]
    target = data[:,1]
    dataSize = data.shape[0]
    cost = 0

    for i in range(0,dataSize):
        y = theta[0]+theta[1]*inp_feature[i]
        cost = cost+(y-target[i])**2

    cost = cost/(2*dataSize)

    print("Cost = "+str(cost))


def gradDesc(data,learningRate,theta,itr):
    dataSize = data.shape[0]
    inp_feature = data[:, 0]
    target = data[:, 1]
    gradTheta0 = 0
    gradTheta1 = 0
    c = 1
    for i in range(0,itr):

        for j in range(0,dataSize):
            gradTheta0 = theta[0] + theta[1]*inp_feature[j] - target[j]
            gradTheta1 = (theta[0] + theta[1] * inp_feature[j] - target[j])*inp_feature[j]

        theta[0] = theta[0] - learningRate*gradTheta0/(2*dataSize)
        theta[1] = theta[1] - learningRate * gradTheta1/(2*dataSize)

        print("Theta0 = "+str(theta[0]))
        print("Theta1 = " + str(theta[1]))
        cost(data,theta)
        print("\n")

    return theta

data = np.array([[1,3],
                 [2,5],
                 [3,7]])




#data = featureScaling(data) #if necessary to scale down data to standarize

learningRate = 1

theta = np.array([5,5])

itr = 100


predictedTheta =  gradDesc(data,learningRate,theta,itr)


x,y = data.T


plt.scatter(x,y)

print(x)

plt.plot(x,predictedTheta[1]*x+predictedTheta[0],'-r')

plt.show()





