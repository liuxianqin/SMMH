from PlayLA.Vector import Vector

if __name__ == "__main__":
    #基本构造
    vec = Vector([5,2,6,7,8])
    vec = Vector([1,2,2,2,2])
    print(vec)
    print(len(vec))
    print("vec[0]={}, vec[1]={}".format(vec[0],vec[1]))
    print()

    #加法
    veca = Vector([5, 2, 6, 7, 8])
    vecb = Vector([1, 2, 2, 2, 2])
    print("{} + {} = {}".format(veca,vecb,veca+vecb))
    print("{} - {} = {}".format(veca, vecb, veca - vecb))
    print("{}*{}={}".format(veca,3,veca*3))
    print("{}*{}={}".format(3,veca, 3*veca))
    print("+{}={}".format(veca,+veca))
    print("-{}={}".format(veca,-veca))

    # 测试零向量
    zero5 = Vector.zero(5)
    print(zero5)
    #取模
    vec2=Vector([3,4])
    print(vec2.norm())
    #单位化
    veck=Vector([3,6])
    try:
        print("{} 单位化后 {}".format(zero5,zero5.normalize()))
    except:
        print("ERROR:zero vector")

    #点×
    vec1=Vector([1,2])
    vec2=Vector([2,3])
    print("******************************************************************************")
    print(vec1.dot(vec2))
    print(Vector.classdot(Vector([1,2,3]),Vector([1,2,3])))
    print("******************************************************************************")

    #加不加方括号
    vecc = Vector(x for x in [1,2,3,4])
    print(vecc)

    a = [1,2,3]
    b = [3,4,5]
    print(a for a in zip(a,b))   #python3,7 地址

    vv1 = Vector([0,1])
    vv2 = Vector([0,3])
    print(vv1 == vv2)


