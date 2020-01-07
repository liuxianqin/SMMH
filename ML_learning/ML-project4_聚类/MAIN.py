import scipy.io as scio
import numpy as np


# 300*2 的矩阵
def loadDateSet(filename):
    data = scio.loadmat(filename)
    return data['X']


def distEuclid(vecA, vecB):
    return np.sqrt(np.sum(np.power(vecA - vecB, 2)))


# 生成随机的质心 k是质心个数
def randCenter(dataSet, k):
    n = np.shape(dataSet)[1]
    centroids = np.mat(np.zeros((k, n)))
    for j in range(n):
        minJ = min(dataSet[:, j])
        rangeJ = float(max(dataSet[:, j]) - minJ)
        centroids[:, j] = minJ + rangeJ * np.random.rand(k, 1)
    return centroids


# 逐步迭代 直到分配结果不再改变
def kMeans(dataSet, k, distFunc=distEuclid, createCenter=randCenter):
    clu_list = []
    m = np.shape(dataSet)[0]
    clusterAssment = np.mat(np.zeros((m, 2)))
    centroids = createCenter(dataSet, k)
    ChangeFlag = True
    while ChangeFlag:
        ChangeFlag = False
        for i in range(m):
            minDist = np.inf
            minIndex = -1
            for j in range(k):
                distJI = distFunc(centroids[j, :], dataSet[i, :])
                # print(distJI)
                if distJI < minDist:
                    minDist = distJI
                    minIndex = j
            if clusterAssment[i, 0] != minIndex:
                ChangeFlag = True
            clusterAssment[i, :] = minIndex, minDist ** 2
        # print(centroids)
        clu_list.append(centroids)
        for center in range(k):
            ptsInClust = dataSet[np.nonzero(clusterAssment[:, 0].A == center)[0]]
            centroids[center, :] = np.mean(ptsInClust, axis=0)
    xylist0 = []
    xylist1 = []
    xylist2 = []
    clusterAssment = clusterAssment.tolist()
    for i in range(len(clusterAssment)):
        if clusterAssment[i][0]==0.0:
            xylist0.append(dataSet[i])
        if clusterAssment[i][0]==1.0:
            xylist1.append(dataSet[i])
        if clusterAssment[i][0]==2.0:
            xylist2.append(dataSet[i])

    print(xylist0[0][0])

    return centroids, clusterAssment, clu_list, xylist0, xylist1, xylist2


# 画图
def draw(dataSet, myroids, clu_list, xylist0, xylist1, xylist2):
    myroids = myroids.tolist()
    from matplotlib import pyplot as plt
    # x = dataMat[:, 0]
    # y = dataMat[:, 1]
    plt.title("K-mains")
    plt.xlabel("x axis caption")
    plt.ylabel("y axis caption")
    # plt.plot(x, y, 'ob')

    # x0 = xylist0[:,0]
    # y0 = xylist0[:,1]
    # plt.plot(x0,y0,'o')

    plt.plot([x[0] for x in xylist0], [y[1] for y in xylist0], 'o')
    plt.plot([x[0] for x in xylist1],[y[1] for y in xylist1],'o')
    plt.plot([x[0] for x in xylist2], [y[1] for y in xylist2], 'o')

    # final
    plt.scatter([x[0] for x in myroids], [y[1] for y in myroids], s=2000,marker='8')

    plt.show()


if __name__ == "__main__":
    filename = 'ex7data2.mat'
    dataMat = loadDateSet(filename)
    myroids, Assing, clu_list, xylist0, xylist1, xylist2= kMeans(dataMat, 3)

    mylist = myroids.tolist()


    print(Assing)


    draw(dataMat, myroids, 3, xylist0, xylist1, xylist2 )




    # n = randCenter(dataMat, 4)
    # print(n)
    # d = distEuclid(np.array([[1,1]]), np.array([[0,0]]))
    # print(d)  #sum and np.sum
