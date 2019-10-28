

import numpy as np
from numpy.linalg import eig

if __name__== "__main__":

    A1 = np.array([[4,-2],[1,1]])
    print(A1)

    eigvalue , eigvector = eig(A1)
    print(eigvalue)
    print(eigvector)    #归一化
    print()


    #复数   python 自带复数
    A3 = np.array([[0,-1],[1,0]])
    e3 , e3vector = eig(A3)
    print(e3)
    print(e3vector)

    A5 = np.array([[3, 1],
                   [0, 3]]);
    eigenvalues5, eigenvectors5 = eig(A5);
    print(eigenvalues5)
    print(eigenvectors5)
    print()


    A_99 = np.array([[1,2,3],[4,5,6]])
    print(A_99.shape)
    print(A_99.ndim)
