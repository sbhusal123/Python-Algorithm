import numpy as np

import matplotlib.pyplot as plt

def cost(data,theta):
    cost = 0
    size = data.shape[0]
    input_feature = data[:, :-1]
    target = data[:, -1]
    for j in range(0, size):
        x = theta[0][0] + theta[0][1] * input_feature[j][0] + theta[0][2] * input_feature[j][1]
        hOftheta = 1 / (1 + np.exp(-x))
        cost = cost +  target[j] *np.log(hOftheta)+(1-target[j])*np.log(1-hOftheta)
    cost = -cost/size

    return cost






def computeTheta(data,theta,itr,learningRate):

    costPoints = np.array([[0,cost(data,theta)]])

    size = data.shape[0]

    input_feature = data[:,:-1]

    target = data[:,-1]


    for i in range(0,itr):
        gradTheta0 = 0
        gradTheta1 = 0
        gradTheta2 = 0
        for j in range(0,size):
            x = theta[0][0] + theta[0][1] * input_feature[j][0] + theta[0][2] * input_feature[j][1]
            hOftheta = 1/(1+np.exp(-x))
            gradTheta0 = gradTheta0 + (hOftheta - target[j])
            gradTheta1 = gradTheta1 + ( hOftheta - target[j]) * input_feature[j][0]
            gradTheta2 = gradTheta2 + (hOftheta - target[j]) * input_feature[j][1]

        theta[0][0] = theta[0][0] - (learningRate * gradTheta0)/size
        theta[0][1] = theta[0][1] - (learningRate * gradTheta1)/size
        theta[0][2] = theta[0][2] - (learningRate * gradTheta2)/size

        c = cost(data,theta)

        costPoints = np.vstack([costPoints,[i,c]])

        print("Iteration = "+str(i))
        print("Theta = "+ str(theta))
        print("Cost = "+str(c))
        print("\n")

    return costPoints,theta


def plot(data,plot1):
    for i in range(0,data.shape[0]):
        if data[i][2] == 0:
            plot1.scatter(data[i][0],data[i][1],marker='^',c='r')
        else:
            plot1.scatter(data[i][0], data[i][1], marker='o', c='b')






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


itr = 10000

theta = np.array([[0.5,0.5,0.5]])

learningRate = 0.05


f ,(plot1,plot2) = plt.subplots(1,2)

costPoints,theta =  computeTheta(data,theta,itr,learningRate)

# ------------------- Calculating the intercept made in x and y axes  for ploting in form x/a+y/b = 1 -------------------------
x_intercept = -theta[0][0]/theta[0][1]
y_intercept = -theta[0][0]/theta[0][2]
print("X-intercept = "+ str(x_intercept))
print("Y-intercept = "+ str(y_intercept))
# --------------------------------------------

plot(data,plot1)  #scatter plott of the actual points
plot2.plot(costPoints[:,0],costPoints[:,1]) #iteration vs cost plot

#POints for plotting line in the form of double-intercept form
x = np.arange(-2,7,1)
y = (x_intercept*y_intercept-y_intercept*x)/x_intercept


plot1.plot(x,y,c='c') #plot intercept lines

plot1.set_title('Decision Line Visualization')
plot1.set_xlabel('X',size=15)
plot1.set_ylabel('Y',size=15)

plot2.set_title('Error Vs Iterations')
plot2.set_xlabel('Iterations',size=15)
plot2.set_ylabel('Cost/Error',size=15)

plt.show()