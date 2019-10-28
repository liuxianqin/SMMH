from .Matrix import Matrix
from .Vector import Vector
from ._global import is_zero

def LU(matrix):

    #只是方阵
    assert matrix.row_num()==matrix.col_num(),"MUST BE SQUARE"

    n = matrix.row_num()
    A = [matrix.row_vector(i) for i in range(n)]
    L = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n) ]   #单位列表

    for i in range(n):

        if is_zero(A[i][i]):
            return None, None
        else:
            for j in range(i+1,n):
                p = A[j][i] / A[i][i]           #系数
                A[j] = A[j]-p*A[i]
                L[j][i] = p

    return Matrix(L),Matrix( [A[i].listback() for i in range(n)] )





