from PlayLA.Matrix import Matrix
from PlayLA.LU import LU

if __name__== "__main__":

    A = Matrix([[1,2,3],[4,5,6],[3,-3,5]])
    L,U = LU(A)
    print(L)
    print(U)