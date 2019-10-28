from PlayLA.Matrix import Matrix
from PlayLA.GramSchmidtProcess import QR

if __name__=="__main__":


    A1 = Matrix( [[1,1,2],[1,1,0],[1,0,0]])
    print(A1)
    Q1,R1 = QR(A1)
    print(Q1,R1)