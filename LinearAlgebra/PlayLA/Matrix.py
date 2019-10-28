from PlayLA.Vector import Vector

class Matrix:

    def __init__(self, list2d):
        if isinstance(list2d[0],list):
            self._values = [row[:] for row in list2d]  #复制list2d中的每一个元素  每个元素是一个列表
            # print("构造的matrix  list", self._values)
        if isinstance(list2d[0],Vector):
            # self._values = [ list2d[i].listback() for i in list2d  ]   #和下面一样吗？
            # print("构造的matrix")
            self._values = [ row.listback() for row in list2d]
            # print("构造的matrix  Vector",self._values)

    @classmethod
    def zero(cls,r,c):
        #bobo: return cls( [[0]*c for _ in range(r)]
        return cls([[0]*c]*r)                #pythonic

    @classmethod
    def identity(cls, n):
        """单位矩阵"""
        m= [[0]*n  for _ in range(n)]
        for i in range(n):
            m[i][i]=1
        return cls(m)

    def __repr__(self):
        return "Matrix({})".format(self._values)
    def __str__(self):
        return "({})".format(self._values)

    def shape(self):
        # 返回(行数，列数)
        return len(self._values),len(self._values[0])
    def row_num(self):
        return self.shape()[0]
    def col_num(self):
        return self.shape()[1]

    def size(self):
        return self.row_num()*self.col_num()

    def __getitem__(self, pos):
        r, c = pos
        return self._values[r][c]

    def row_vector(self, index):
        #返回行向量
        return Vector(self._values[index])
    def col_vector(self, index):
        # col_list = []

        # return Vector([x for x in self._values])
        return Vector([row[index] for row in self._values])


    #运算
    def __add__(self, other):
        assert self.shape()==other.shape(),"ERROR is adding: shape of matrix must be same"
        # return Matrix([a+b for a,b in zip(self._values,other._values)])
        return Matrix( [   [a+b for a,b in zip(self.row_vector(i),other.row_vector(i))]  for i in range(self.row_num())  ]  )
    def __sub__(self, other):
        assert self.shape()==other.shape(),"ERROR is subtracting.shape of matrix must be same"
        return Matrix([[a-b for a,b in zip(self.row_vector(i),other.row_vector(i))] for i in range(self.row_num())])
    def __mul__(self, k):
        return Matrix([[k*row_vector for row_vector in self.row_vector(i)] for i in range(self.row_num())])
    def __rmul__(self, k):
        return self*k
    def __truediv__(self, k):
        return 1/k*self
    def __pos__(self):
        return 1*self
    def __neg__(self):
        return -1*self;

    def dot(self, other):
        """返回矩阵的乘法"""
        if isinstance(other, Vector):
            assert self.col_num()==len(other),"CAN NOT dot"
            # return Vector([Vector(row_vector)*row_elem for row_vector,row_elem in zip(self._values,other)])
            # return Vector([a.dot(b) for a in self.row_vector(i) for b in other] for i in range(self.row_num()) )
            return Vector([self.row_vector(i).dot(other) for i in range(self.row_num())])
        if isinstance(other, Matrix):
            assert self.col_num()==other.row_num(),"can not dot"
            return Matrix([ [self.row_vector(i).dot(other.col_vector(j)) for j in range(other.col_num()) ] for i in range(self.row_num()) ])

    def T(self):
        # return Matrix([elem for elem in self.col_vector(i)] for i in range(self.row_num()))
        # bobo: return Matrix([[e for e in self.col_vector(i)] for i in range(self.col_num())])
        return         Matrix([[elem for elem in self.col_vector(i)] for i in range(self.col_num())])
        #                       在这里加不加【】
        # Matirx( [ ] for i in range(n) )
        # Matrix([[ ] for i in rangen() ])
    #
    # a = [1, 2, 3]
    # >> > b = a[i]
    # for i in range(3)
    #     File
    #     "<stdin>", line
    #     1
    #     b = a[i]
    #     for i in range(3)
    #         ^
    #     SyntaxError: invalid
    #     syntax
    #     >> > b = a[i]
    #     for i in range(3)
    #         File
    #         "<stdin>", line
    #         1
    #         b = a[i]
    #         for i in range(3)
    #             ^
    #         SyntaxError: invalid
    #         syntax
    #         >> > b = [a[i] for i in range(3)]
    #         >> > b
    #         [1, 2, 3]

