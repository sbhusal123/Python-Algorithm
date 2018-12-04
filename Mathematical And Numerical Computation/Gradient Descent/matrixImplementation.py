import numpy as np
import matplotlib.pyplot as plt

def regression(data):

    size = data.shape[0]
    unit = np.ones([size,1])
    data = np.append(unit,data,axis=1)


    x = data[:,0:data.shape[1]-1]

    y = data[:,data.shape[1]-1]


    theta = np.linalg.pinv(x.T*x)*x.T*y

    return theta



data = np.matrix([[1,2],
                [3,5],
                [5,6],
                [4,2],
                [7,9],
                [10,24],
                [50,24],
                [7,4],
                [6,10]
                ])

x,y = data.T

theta =  np.asarray(regression(data))

print(theta)

data = np.asarray(data)


x,y = data.T

plt.xlabel('X')

plt.ylabel('Y')


plt.scatter(x,y) #scattering actual point
plt.plot(x,theta[0][0]+theta[1][0]*x,'-r') #plotting the actual line
plt.show()

