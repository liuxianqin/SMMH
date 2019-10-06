import numpy as np
from  numpy.linalg import eig,inv
from PlayLA.LinearSystem import rank
from PlayLA.Matrix import Matrix

def diagonalize(A):

    assert A.ndim ==2
    assert A.shape[0]==A.shape[1]

    eigvalues , eigvectors = eig(A)

    P = eigvectors
    if rank(   Matrix(P.tolist())  ) != A.shape[0]:
        print("不可逆")
        return None,None,None
    D = np.diag(eigvalues)
    Pinv = inv(P)

    return P,D,Pinv

if __name__ == "__main__":
    A1 = np.array([[4, -2], [1, 1]])
    P1,D1,P1inv = diagonalize(A1)
    print(P1)
    print(D1)
    print(P1inv)

    #不能对角化的情况
    A2 = np.array([[3,1],[0,3]])
    P2, D2, P2inv = diagonalize(A2)
    print(P2)
    print(D2)
    print(P2inv)                                   #大大大大大

