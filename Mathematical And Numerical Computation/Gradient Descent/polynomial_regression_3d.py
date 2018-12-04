import  numpy as np
from matplotlib import  pyplot as plt

#still having the problem with convergence

def generateData():

    d = np.array([[0,0,0.5]])
    x0 = np.array([0.1, 0.4, 0.6, 0.8,0.12,0.54,0.23,0.201,0.23,0.45])
    x1 = np.array([0.4, 0.6, 0.2, 0.1,0.23,0.43,0.54,0.320,0.12,0.44])

    for i in range(0,x0.shape[0]):
        k = 0.2*np.power(x1[i],2)+0.3*x0[i]+0.5
        d = np.vstack([d,[x0[i], x1[i], k]])

    return d

def cost(data,theta):
    c = 0

    feature_Size = data.shape[1] - 1
    size = data.shape[0]
    input_feature = data[:, 0:feature_Size]
    target = data[:, feature_Size]

    for i in range(0,size):
        c = (theta[0][0] + input_feature[i][0] * theta[0][1] + input_feature[i][1] * theta[0][2] - target[i])**2
    return c/(2*size)


def computeTheta(data,theta,itr,learningRate):


    cost_points = np.array([[0,cost(data,theta)]])

    feature_Size = data.shape[1] -1
    size = data.shape[0]

    input_feature = data[:,0:feature_Size]

    target = data[:,feature_Size]


    gradTheta0 = 0
    gradTheta1 = 0
    gradTheta2 = 0

    for i in range(0,itr):
        for j in range(0,size):
            gradTheta0 = (theta[0][0] + input_feature[j][0] * theta[0][1] + np.power(input_feature[j][1],2) * theta[0][2] - target[j])
            gradTheta1 = (theta[0][0] + input_feature[j][0] * theta[0][1] + np.power(input_feature[j][1],2) * theta[0][2] - target[j]) * input_feature[j][0]
            gradTheta2 = (theta[0][0] + input_feature[j][0] * theta[0][1] + np.power(input_feature[j][1],2) * theta[0][2] - target[j]) * np.power(input_feature[j][1],2)

        theta[0][0] = theta[0][0] - (gradTheta0 * learningRate)/2*size
        theta[0][1] = theta[0][1] - (gradTheta1 * learningRate)/2*size
        theta[0][2] = theta[0][2] - (gradTheta2 * learningRate)/2*size

        c = cost(data, theta)

        print("Cost = "+str(c))

        print("Theta = "+str(theta))

        print("\n")

        cost_points = np.vstack([cost_points, [i, c]])

    return [theta,cost_points]






# data = np.array([[0.1, 0.1,5.12 ],
#                  [0.2, 0.3, 5.38]])

data = generateData()

print(data)


theta = np.array([[0.1,0.1 ,0.1]])

itr = 5000

learningRate = 0.005



[theta,cost_points] =  computeTheta(data, theta, itr, learningRate)


plt.plot(cost_points[:,0],cost_points[:,1])


print(theta)

plt.show()
