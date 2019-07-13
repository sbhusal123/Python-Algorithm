
import numpy as np
import matplotlib.pyplot as plt

class KmeansClustering:

    def dataAttribites(self,data):
        self.rows = data.shape[0]
        self.cols = data.shape[1]



    def initializeCentroidAndClusters(self):
        self.cluster_centeroid = np.zeros((self.n_clusters,self.cols)) #initialization for array holding center for each clusters

        #https://stackoverflow.com/questions/14262654/numpy-get-random-set-of-rows-from-2d-array

        random = np.random.choice(self.rows,size=n_cluster,replace=False) #random selection of  cluster centroid from data points
        self.cluster_centeroid = data[random,:]


        print(self.cluster_centeroid)

        # initialize the empty list for storing the sulists of n_clusters points
        self.cluster_points_list = [[] for i in range(self.n_clusters)]

        # point is assigned to the [n] cluster if the distance from [n] cluster to data point is comparatavely minimum
        self.distance = np.zeros(self.n_clusters)

        # initialize mean of the data in the specific clusters
        self.means = np.zeros(self.n_clusters)

    def calculateDistance(self,data_point,center):
        return np.linalg.norm(data_point - center)

    def startClustering(self,itr):
        for itr in range(0,itr):

            #clearing the previous points in the clusters we only need the clusters centers
            for i in range(0, self.n_clusters):
                if len(self.cluster_points_list[i]) != 0:
                    self.cluster_points_list[i].clear()


            for j in range(0,self.rows):

                for k in range(0,self.n_clusters):
                    self.distance[k] = self.calculateDistance(self.data[j,:],self.cluster_centeroid[k,:])

                min_distance_cluster =  list(self.distance).index(np.min(self.distance)) #from which center distance is minimum

                self.cluster_points_list[min_distance_cluster].append(data[j,:])

            #updating the cluster centroid
            for k in range(0,self.n_clusters):
                self.cluster_centeroid[k] = np.mean(self.cluster_points_list[k])


            print("\n")
            print("Iteration = " + str(itr))
            print("________________________________________________________________________________\n")
            for k in range(self.n_clusters):
                print("Cluster " + str(k) + "= " + str(self.cluster_points_list[k]))
            print("________________________________________________________________________________\n")





    def __init__(self,n_clusters):
        self.n_clusters = n_clusters



    def  fit(self,data):
        self.data = data
        self.dataAttribites(data)
        self.initializeCentroidAndClusters()






data = np.array([[1,2],
                 [4,5],
                 [6,7],
                 [8,9]])

n_cluster = 2

k = KmeansClustering(n_clusters=n_cluster)

k.fit(data)

k.startClustering(5)
















