import numpy as np

if __name__=="__main__":

    print(np.__version__)

    vec = np.array([1,2,3])
    print(vec)
    print(vec)  #可更改

    #零向量
    print(np.zeros(5))

    print(np.ones(5))

    print(np.full(5,10))

    print("size=",vec.size)
    print("size=",len(vec))
    print(vec[-1])
    print(vec[0:2])
    print(type(vec[0:2]))

    #逐个元素的乘法
    vec1=np.array([1,2,3])
    vec2=np.array([4,5,6])
    print("{} * {} = {}".format(vec1,vec2,vec1*vec2))
    print("{}.dot({})={}".format(vec1,vec2,vec1.dot(vec2)))

    #求模
    print(np.linalg.norm(vec1))
    #归一化
    print(vec1/np.linalg.norm(vec1))

    vec0=np.zeros(3)
    # print(vec0/np.linalg.norm(vec0)) [nan nan nan]
    # /home/user/PycharmProjects/LinearAlgebra/main_numpy_vector.py:36: RuntimeWarning: invalid value encountered in true_divide
    #   print(vec0/np.linalg.norm(vec0))


