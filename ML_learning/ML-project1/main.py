#coding='utf-8'
import numpy as np
import matplotlib.pyplot as plt

plt.xlim(0, 20)
plt.ylim(0, 20)

thefile = "data1a.txt"

population = []
profit = []
pp=[]
epsilon = 0.00001
error0 = 0.0

with open(thefile, 'r') as f:
    lines = f.readlines()
    # print(lines)
    for line in lines:
        line=line.strip('\n')
        odom = line.split(',')
        # print(odom)
        a = map(float,odom)
        pp.append(list(a))
population = [elem[0] for elem in pp]
profit = [elem[1] for elem in pp]

print("population",population)
print("profit",profit)
plt.scatter(population,profit)
xb =  [0]*len(population)

print(xb)
xt = [ i for i in  zip(population,xb) ]
xt_list = [list(i) for i in xt ]
print(xt_list)

#y=2 * (x1) + (x2) + 3
rate = 0.0001
x_train = np.array(xt_list)
y_train = np.array(profit)
x_test  = np.array([    [3.5],    [7]  ])

a = np.random.normal()
c = np.random.normal()     #

print("a:",a,"c:",c)

def h(x):
    return a*x[0]+c

for i in range(100):
    sum_a=0
    sum_c=0
    for x, y in zip(x_train, y_train):
        sum_a = sum_a + rate*(y-h(x))*x[0]
        sum_c = sum_c + rate*(y-h(x))
    a = a + sum_a
    c = c + sum_c

    # 画出每次迭代的回归直线
    xx1 = 0
    yy1 = c
    xx2 = 100
    yy2 = xx2 * a + c
    plt.plot([xx1, xx2], [yy1, yy2])

    # 计算损失函数
    theta0=a
    theta1=c
    error1 = 0
    for lp in range(len(population)):
        print( "J()", error1 )
        error1 += (profit[lp] - (theta0 + theta1 * xt_list[lp][0] )) ** 2 / 2

    if abs(error1 - error0) < epsilon:
        print("最终的J（）", error1)
        break
    else:
        error0 = error1


xx1=0
yy1=c
xx2=100
yy2=xx2*a+c
plt.plot([xx1,xx2],[yy1,yy2])


print("final a",a)
print("final c",c)

# result=[h(xi) for xi in x_train]
# print(result)

result=[h(xi) for xi in x_test]
print(result)                       #[1.8811019499784092, 5.188371747183096]
                                    #[0.27983694830023254, 4.455454663946947] 10000time
                                    #[1.8989315033512955, 5.196532535209915] 100000time


# plt.scatter([1,2,3,4],[1,2,3,4])
plt.show()

