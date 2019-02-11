# Algorithm at: https://www.saedsayad.com/clustering_kmeans.htm
#This is non optimized version using the Data-Structure

import numpy as np



def KMeansClustering(data,n_clusters,verbose):

    no_samples = data.shape[1] #size of the data points

    cluster_center = np.zeros(n_clusters)  # clusters centers array initialization

    #randomly assigning the cluster center
    for i in range(0,n_clusters):
        cluster_center[i] = data[0][np.random.randint(0,no_samples-2)]



    # initialize the empty list for storing the sulists of n_clusters points
    cluster_points_list = [[] for i in range(n_clusters)] #note


    #point is assigned to the [n] cluster if the distance from [n] cluster to data point is comparatavely minimum
    distance = np.zeros(n_clusters)

    #initialize mean of the data in the specific clusters
    means = np.zeros(n_clusters)


    for iter in range(0,5): #run in iterations: but actually must check whether the two points in list are equal or not
        # runing the loop is not good in professional practice. Must check whether the previous cluster = new cluster

        #clear the previous points in the clusters
        for i in range(0, n_clusters):
            if len(cluster_points_list[i]) != 0:
                cluster_points_list[i].clear()

        #assign the new points to the clusters
        for  i in range(0,no_samples):
            for j in range(0,n_clusters):
                distance[j] = np.abs(cluster_center[j]-data[0][i])
            toWhichCluster = list(distance).index(np.min(distance)) #to which cluster does the specific data point to be added

            cluster_points_list[toWhichCluster].append(data[0][i])

        for i in range(0,n_clusters):
            if len(cluster_points_list[i]) != 0:
                cluster_center[i] = np.mean(cluster_points_list[i])

        if verbose == True:
            print("\n")
            print("Iteration = "+str(iter))
            print("________________________________________________________________________________\n")
            for k in range(n_clusters):
                print("Cluster "+str(k)+"= "+str(cluster_points_list[k]))
            print("________________________________________________________________________________\n")

    return cluster_points_list



# x = np.array([[15,15,16,19,19,20,20,21,22,28,35,40,41,42,43,44,60,61,65]])

x = np.array([[2,1,3,5,4,7,6,8,9,0,10]])

clusters = KMeansClustering(x,5,verbose=True)














