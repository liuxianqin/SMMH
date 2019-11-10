import scipy.io as scio
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split

data = scio.loadmat('ex3data1.mat')
X = data['X']
Y = data['y'].flatten()
C_list=[0.01,0.03,0.1,0.3,1,3,10,30]
gamma_list=[0.01,0.03,0.1,0.3,1,3,10,30]


#  计算正确率
def yes_percent(check_list, label_list):
    sum = len(Y)
    wrong = 0
    check_ans = list(zip(check_list, label_list))
    for i in check_ans:
        if i[0] != i[1]:
            wrong += 1
    return "\t正确率 " + str((1 - wrong / sum) * 100) + "%"


#划分训练样本与测试样本, 20%的样本作为测试集
x_train,x_test,y_train,y_test=train_test_split(X,Y, random_state=1, test_size=0.2)
# #设置SVM参数C,核函数，gamma值，此处仅设置一个组合，需补充其他组合
# clf = svm.SVC(C=1, kernel='rbf', gamma=1)
# #利用x_train , y_train 训练SVM分类器，获得参数。
# clf.fit(x_train, y_train)
# #预测测试集图像的标签
# y_predict=clf.predict(x_test)
#
# # print(y_predict)
# print(yes_percent(y_predict,y_test))



def redo():
    for c in C_list:
        for gamma in gamma_list:
            # 设置SVM参数C,核函数，gamma值，此处仅设置一个组合，需补充其他组合
            clf = svm.SVC(C=c, kernel='rbf', gamma=gamma)
            # 利用x_train , y_train 训练SVM分类器，获得参数。
            clf.fit(x_train, y_train)
            # 预测测试集图像的标签
            y_predict = clf.predict(x_test)
            per = yes_percent(y_predict, y_test)

            # y_predict = np.array(y_predict)
            # y_test = np.array(y_test)
            print(y_predict)
            print(y_test)
            # print('Training set accuracy: {}'.format(np.mean(y_predict == y_test) * 100))
            print( "C:{c:>5} ,gamma={gamma:>4}, {per}".format(c=c,gamma=gamma,per=per)          )


redo()
# for c in C_list:
#     for gamma in gamma_list:
#         # print("C=" + str(c) + "\t\t\t" + "\tgamma=" + str(gamma) + "\t\t\t", "\t\t\tHELLO")
#         print( "C:{c:>5} ,gamma={gamma:>4}, 正确率={per}".format(c=c,gamma=gamma,per="HRLLO")          )