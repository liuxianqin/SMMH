#coding=utf-8

from skimage import data
import skimage.morphology as sm
import matplotlib.pyplot as plt


img=data.checkerboard()
dst1=sm.dilation(img,sm.square(5))  #用边长为5的正方形滤波器进行膨胀滤波
dst2=sm.dilation(img,sm.square(15))  #用边长为15的正方形滤波器进行膨胀滤波

plt.figure('morphology',figsize=(8,8))
plt.subplot(131)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)

plt.subplot(132)
plt.title('morphological image')
plt.imshow(dst1,plt.cm.gray)

plt.subplot(133)
plt.title('morphological image')
plt.imshow(dst2,plt.cm.gray)
