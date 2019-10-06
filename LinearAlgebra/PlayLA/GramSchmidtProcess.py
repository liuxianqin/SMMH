#
from .Vector import Vector
from .Matrix import Matrix
from .LinearSystem import rank

#
def gram_schmidt_process(basis):

    #验证是不是一组基
    matrix = Matrix(basis)

    # print("zhi",rank(matrix))
    # print("基的维度",len(basis))
    assert rank(matrix)==len(basis)

    res = [basis[0]]

    for i in range(1,len(basis)):
        p = basis[i]
        for r in res:
            # p = p - basis[i].dot(r) / r.norm()**2
            p = p - basis[i].dot(r) / r.dot(r) *r
        res.append(p)

    return res


def QR(A):

    assert A.row_num()==A.col_num(),"Must be square"
    basis = [A.col_vector(i) for i in range(A.col_num())]
    P = gram_schmidt_process(basis)
    print("P",P)
    Q = Matrix([v / v.norm() for v in P]).T()
    R = Q.T().dot(A)
    return Q,R
