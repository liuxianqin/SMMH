from .Matrix import Matrix
from .Vector import Vector
from ._global import is_zero

class LinearSystem:

    def __init__(self, A, b=None):
        self._m = A.row_num()
        self._n = A.col_num()

        if b is None:
            self.Ab = [A.row_vector(i) for i in range(A.row_num())]

        if isinstance(b,Vector):
            assert A.row_num() == len(b), "ERROR row number of A must be equal to the lenth of b"
            # self.Ab = [ Vector(A.row_vector(i).listback() + [b[i]]) for i in range(self._m) ])
            self.Ab = [ Vector( A.row_vector(i).listback() + [b[i]] ) for i in range(self._m) ]
        if isinstance(b,Matrix):
            #b 的行向量还加不加【】 a = [1,2,3]
            # >>> b =[3,4,5]
            # >>> a+b
            # [1, 2, 3, 3, 4, 5]
            # >>> a+[b]
            # [1, 2, 3, [3, 4, 5]]
            self.Ab = [ Vector( A.row_vector(i).listback() +  b.row_vector(i).listback()   ) for i in range(self._m) ]

        #主元
        self.pivots = []

    def _max_row(self,index_i,index_j, n):
        best, ret= self.Ab[index_i][index_j], index_i
        for i in range(index_i+1,n):
            if self.Ab[i][index_j]>best:
                best, ret = self.Ab[i][index_j],i
        return ret


    def _forward(self):

        #n = self._m
        i, k = 0, 0
        while i<self._m and k< self._n:
            #主要的元A[i][i]
            #寻找最大主元
            max_row = self._max_row(i,k,self._m)
            self.Ab[i],self.Ab[max_row] = self.Ab[max_row],self.Ab[i]
            #主元变成1

            # print(self.Ab[i])
            # print("类型",self.Ab[i][k])
            if is_zero(self.Ab[i][k]):
                k += 1
            else:
                self.Ab[i] = self.Ab[i]/self.Ab[i][k]    #ab[i][i]==0?
                #   下方变成0
                for j in range(i+1, self._m):
                    self.Ab[j] = self.Ab[j] - self.Ab[j][k]*self.Ab[i]
                self.pivots.append(k)
                i +=1

    def _backward(self):
        n = len(self.pivots)
        for i in range(n-1,-1,-1):
            k = self.pivots[i]
            for j in range(i-1, -1 ,-1):
                self.Ab[j] = self.Ab[j] - self.Ab[j][k]*self.Ab[i]

    def gauss_jordan_elimination(self):

        self._forward()
        self._backward()
        #第一个非0行的位置
        #搜出全0行
        for i in range(len(self.pivots),self._m):
            if not is_zero(self.Ab[i][-1]):
                return False
        return True

    def fancy_print(self):

        for i in range(self._m):
            print(" ".join(str(self.Ab[i][j]) for j in range(self._n) ),end = " ")
            print("|",self.Ab[i][-1])


def inv(A):

    if A.row_num() != A.col_num():
        return None
    n = A.row_num()

    ls = LinearSystem(A,Matrix.identity(n))
    if not ls.gauss_jordan_elimination():
        return None
    invA = [  ls.Ab[i][-n:]  for i in range(n)  ]
    # invA = [[row[i] for i in range(n, 2*n)] for row in ls.Ab]       #bobo
    return Matrix(invA)

def rank(A):

    ls = LinearSystem(A)
    ls.gauss_jordan_elimination()

    zero_row = Vector.zero(A.col_num())
    return sum( row != zero_row for row in ls.Ab)         #需要重载矩阵的不等号