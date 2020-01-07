import scipy.io as scio
import matplotlib.pyplot as plt

from sklearn import decomposition


def loadDataSet(filename):
    data = scio.loadmat(filename)
    return data['X']

def drawOri(dataSet):
    x = dataSet[:,0]
    y = dataSet[:,1]




    
    plt.plot(x, y, 'ob')
    plt.show()




if __name__ == "__main__":

    filename = 'ex7data1.mat'
    x = loadDataSet(filename)

    pca = decomposition.PCA()

    pca.fit(x)
    plt.plot(pca.explained_variance_, 'k', linewidth=2)
    plt.show()
    # drawOri(x)

