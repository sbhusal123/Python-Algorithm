import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import  Axes3D
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
    return cost


def gradDesc(data,learningRate,theta,itr):
    threeD_plot_points = np.array([[theta[0],theta[1],cost(data,theta)]],dtype=float)
    c = np.array([[0,cost(data,theta)]],dtype=float)

    dataSize = data.shape[0]
    inp_feature = data[:, 0]
    target = data[:, 1]
    gradTheta0 = 0
    gradTheta1 = 0
    for i in range(0,itr):
        gradTheta0 = 0
        gradTheta1 = 0
        for j in range(0,dataSize):
            gradTheta0 = gradTheta0 + theta[0] + theta[1]*inp_feature[j] - target[j]
            gradTheta1 = gradTheta1 + (theta[0] + theta[1] * inp_feature[j] - target[j])*inp_feature[j]

        theta[0] = theta[0] - learningRate*gradTheta0/(2*dataSize)
        theta[1] = theta[1] - learningRate * gradTheta1/(2*dataSize)

        print("Theta0 = "+str(theta[0]))
        print("Theta1 = " + str(theta[1]))
        k =  cost(data,theta)
        c = np.vstack([c,[i,k]])
        threeD_plot_points = np.vstack([threeD_plot_points,[theta[0],theta[1],k]])
        print("\n")

    return theta,c,threeD_plot_points

#generating random 2d array
mean = [1, 2]
cov = [[8, -5], [0.2, 0.2]]
data = np.random.multivariate_normal([0, 2], cov, 300)

# data= featureScaling(data)



learningRate = 0.001
theta = np.array([2,-0.5])
itr = 1000

[predictedTheta,cost_points,threeD_plotpoints] =  gradDesc(data,learningRate,theta,itr)
x,y = data.T #consists of the points for plotting the equation of line in plots




fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(threeD_plotpoints[:,0], threeD_plotpoints[:,1], threeD_plotpoints[:,2],'-g')
ax.set_xlabel('Theta0')
ax.set_ylabel('Theta1')
ax.set_zlabel('Cost')





f, (plot1,plot2) = plt.subplots(1,2)


plot1.scatter(x,y) #plotting of the actual points
plot1.plot(x,predictedTheta[1]*x+predictedTheta[0],'-r') #plotting of the line we've got
plot1.set_xlabel('X',size=10)
plot1.set_ylabel('Y',size=10)
plot1.set_title('Original Points and Regression Line',size=12)




print('\n')



plot2.plot(cost_points[:,0],cost_points[:,1],'-g')
plot2.set_xlabel('Iterations',size=10)
plot2.set_ylabel('Cost/Error',size=10)
plot2.set_title('Iteration Vs Cost',size=12)
plt.show()


