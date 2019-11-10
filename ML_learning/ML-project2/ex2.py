# coding = utf-8

import scipy.io as scio
import random
import matplotlib.pyplot as plt
import numpy as np

data = scio.loadmat('ex3data1.mat')
X = data['X']
Y = data['y']
y_list = [i[0] for i in Y]
weight = scio.loadmat('ex3weights.mat')
theta1 = weight['Theta1']
theta2 = weight['Theta2']


# 随机选择则100个数字图像
def random_select(X):
    # slist = [i for i in range(100)]
    slist = [random.randint(0,5000) for _ in range(100)]
    print(len(slist), slist)
    newX = []
    for i in slist:
        newX.append(X[i])
    return newX


#  计算正确率
def yes_percent(check_list, Y):
    sum = len(Y)
    wrong = 0
    check_ans = list(zip(check_list, Y))
    for i in check_ans:
        if i[0] != i[1]:
            wrong += 1
    return "正确率" + str((1 - wrong / sum) * 100) + "%"


def sigmoid(z):
    return 1 / (1 + np.exp(-z))




#  传入X[index]   1行400列  一共5000个
def NN(index):
    mat1 =[1] + X[index].tolist()         #  变成 shape = (1,401)
    mat1 = np.array([mat1])
    r1 = mat1.dot(theta1.T)
    a1 = sigmoid(r1)
    # print(a1)
    mat2 =[1] + a1[0].tolist()           # 变成 shape = (1 ,26)
    mat2 = np.array([mat2])
    # print(mat2.shape)
    r2 = mat2.dot(theta2.T)
    a2 = sigmoid(r2)
    # print(a2.shape)
    print(a2)

    #找出10个数中的最大值
    re = np.argmax(a2, axis=1) + 1
    print(re)
    print(Y[index])
    print("\n")
    # print(X[index].shape, theta1.T.shape, theta2.T.shape)
    return re[0]


# 神经网络
def net():
    result_list = []
    # 对每一个图片求一个结果
    for i in range(5000):
        result_list.append(NN(i))

    return result_list


# 函数说明：把输入的图像数据X进行重新排列，显示在一个面板figurePane中，
# 面板中有多个小imge用来显示每一行数据

def display_data(x):
    (m, n) = x.shape

    print('shape:', m, n)
    # 设置每个小图例的宽度和高度
    width = np.round(np.sqrt(n)).astype(int)
    height = (n / width).astype(int)

    # 设置图片的行数和列数
    rows = np.floor(np.sqrt(m)).astype(int)
    cols = np.ceil(m / rows).astype(int)

    # 设置图例之间的间隔
    pad = 1

    # 初始化图像数据
    display_array = -np.ones((pad + rows * (height + pad),
                              pad + cols * (width + pad)))

    # 把数据按行和列复制进图像中
    current_image = 0
    for j in range(rows):
        for i in range(cols):
            if current_image > m:
                break
            # [:,np.newaxis]可以让指定的那一列数据以列的形式返回和指定
            # 否则返回的是行的形式
            max_val = np.max(np.abs(x[current_image, :]))
            display_array[pad + j * (height + pad) + np.arange(height),
                          pad + i * (width + pad) + np.arange(width)[:, np.newaxis]] = \
                x[current_image, :].reshape((height, width)) / max_val
            current_image += 1
        if current_image > m:
            break
    print("pic:", display_array)
    # 显示图像
    plt.figure()
    # 设置图像色彩为灰度值，指定图像坐标范围
    plt.imshow(display_array, cmap='gray', extent=[-1, 1, -1, 1])
    print(display_array)
    plt.axis('off')
    plt.title('Random Seleted Digits')
    plt.show()


if __name__ == "__main__":
    data = scio.loadmat('ex3data1.mat')

    X = data['X']
    Y = data['y']

    print(X)
    print(Y)

    y_list = [i[0] for i in Y]
    print('y_list:', y_list)

    a = np.array(random_select(X))
    print(a)
    display_data(a)

    final = yes_percent(net(), y_list)
    print(final)

    # print(X[0])