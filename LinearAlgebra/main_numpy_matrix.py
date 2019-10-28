import numpy as np

if __name__ == "__main__":
    A = np.array([[1,2,3],[4,5,6]])
    print(A)
    print(A.shape)
    print(A.T)

    print(A[1,1])
    print(A[0])

    #列向量
    print(A[:,0])

    #广播
    p=np.array([[1,1,1]])
    print(A+p)
    print(A+100)

    #单位举证
    I = np.identity(5)
    print(I)

    #逆矩阵
    B = np.array([[1,2],[3,4]])
    invB = np.linalg.inv(B)
    print(invB)

    print(B.dot(invB))
    print(invB.dot(B))  #[[1.0000000e+00 0.0000000e+00]
                        #  [8.8817842e-16 1.0000000e+00]]
                        # [[1.00000000e+00 0.00000000e+00]
                        #  [1.11022302e-16 1.00000000e+00]]




