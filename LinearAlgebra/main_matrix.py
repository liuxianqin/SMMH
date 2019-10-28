from PlayLA.Matrix import Matrix
from PlayLA.Vector import Vector

if __name__=="__main__":

    mat = Matrix([[1,2,3],[4,5,6]])
    print(mat)
    print(mat.shape())
    print(mat.row_num())
    print(mat.col_num())
    print(mat.size())

    print(mat.__getitem__((1,1)))
    print(mat[1,1])

    print(mat.row_vector(1))
    print(mat.col_vector(2))

    mat1=Matrix([[1,2,3],[4,5,6]])
    mat2=Matrix([[2,3,4],[1,1,1]])
    print(mat1+mat2)
    print(mat1-mat2)
    print(mat1*3)
    print(3*mat1)
    print(mat1/2)
    print(-mat2)

    print(Matrix.zero(2,4))
    print(mat1+Matrix.zero(2,3))

    print("***************8")
    print(mat1.dot(Vector([1,1,8])))


    print("矩阵乘法")
    mata=Matrix([[1,2,3],[1,99,3],[3,4,5]])
    matb=Matrix([[1,2,4],[4,4,6],[9,8,9]])
    print(mata.dot(matb))
    print(mata.dot(matb).T())

    T=Matrix([[1.5,0],[0,2]])
    P=Matrix([[0,4,5],[0,0,3]])
    print(T.dot(P))

    #单位举证
    I=Matrix.identity(3)
    print(mata.dot(I))
    print(I.dot(mata))

