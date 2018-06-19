import numpy as np
import matplotlib.pyplot as plt
import random


def create_cluster(X, centroid_pts):
    cluster = {}
  # read about lambdas and np.linalg.form
  # https://stackoverflow.com/questions/32141856/is-norm-equivalent-to-euclidean-distance ,
  # here we are using order 1 to calculate normalized distance
    for x in X:
        value = min([(i[0],np.linalg.norm(x - centroid_pts[i[0]]))for i in enumerate(centroid_pts)], key=lambda s:s[1])[0]
        try:
            cluster[value].append(x)
        except:
            cluster[value] = [x]
    return cluster


def calculate_new_center(cluster):
    keys =sorted(cluster.keys())
    newmu = np.array([(np.mean(cluster[k],axis = 0))for k in keys])
    return newmu

def matched(new_centroids, old_centroids):
    return (set([tuple(a)for a in new_centroids]) == set([tuple(a)for a in old_centroids]))

def Apply_Kmeans(X, K, N):
    # selecting random centroids from dataset and by number of clusters.
    old_centroids = np.random.randint(N, size = K)
    old_centroid_pts = np.array([X[i]for i in old_centroids])

    print("old centroids :",old_centroids)
    print("old centroid ponts:", old_centroid_pts)

    cluster_info = create_cluster(X, old_centroid_pts)

    print("Initial cluster information:")
    print(cluster_info)

    new_centroid_pts=calculate_new_center(cluster_info)
    print("new centroid points :", new_centroid_pts)
    itr = 0
    print("Graph after selecting initial clusters with initial centroids:")
    plot_cluster(old_centroid_pts,cluster_info,itr)
    while not matched(new_centroid_pts, old_centroid_pts):
        itr = itr + 1
        old_centroid_pts = new_centroid_pts
        cluster_info = create_cluster(X,new_centroid_pts)
        plot_cluster(new_centroid_pts, cluster_info,itr)
        new_centroid_pts = calculate_new_center(cluster_info)

    print("Results after final iteration:")
    plot_cluster(new_centroid_pts, cluster_info, itr)
    return

def plot_cluster(mu,cluster, itr):
    color = 10 * ['r.','g.','k.','c.','b.','m.']
    print('Iteration number : ',itr)
    for l in cluster.keys():
        for m in range(len(cluster[l])):
            plt.plot(cluster[l][m][0], cluster[l][m][1], color[l], markersize=10)
    plt.scatter(mu[:,0],mu[:,1],marker = 'x', s = 150, linewidths = 5, zorder = 10)
    plt.show()

def init_graph(N, p1, p2):
    X = np.array([(random.randint(p1,p2),random.randint(p1,p2))for i in range(N)])
    print(X)
    return X

def Simulate_Clusters():
    print(".........Small, Medium and Large are the T-shirt sizes.........")
    Number_of_points = 7
    Number_of_clusters = 3#int(input('Enter the number of Clusters.......'))
    print('Below are lower and upper bound details for the points in each cluster\n')
    points_lower_bound = 100
    points_upper_bound = 200
    #X = init_graph(Number_of_points, points_lower_bound, points_upper_bound)
    X = np.array(
        [[5, 35], [6, 15], [5, 102], [5, 100], [30, 145], [8, 170], [5, 80], [6, 178], [5, 152], [4, 100], [5, 145],
         [8, 170], [7, 80], [6, 78], [6, 62], [4, 50], [55, 145], [65, 78], [71, 130], [60, 78], [55, 32], [42, 40],
         [30, 45], [85, 70], [71, 80], [6, 8], [45, 52], [80, 91], ])
    # plot them on the graph
    plt.scatter(X[:, 0], X[:, 1], label='True Position')
    #X = np.array([2,3], [4,2], [1,6],[5,4])
    #plt.scatter(X[:, 0], X[:, 1],)
    plt.show()
    temp = Apply_Kmeans(X, Number_of_clusters, Number_of_points)



if __name__ == '__main__':
    Simulate_Clusters()
