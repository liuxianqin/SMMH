import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import skimage.color as sc
from matplotlib.pyplot import imshow

i=np.array(Image.open('img.jpg'))
img=Image.open('img.jpg')
i_mono=sc.rgb2gray(i)
#plt.show(img)
#plt.imshow(i_mono,cmap='gray')
def im_hist(img):
    fig=plt.figure(figsize=(8,6))
    fig.clf()
    ax=fig.gca()
    ax.hist(img.flatten(),bins=256)
    plt.show()

#im_hist(i_mono)

def im_cdf(img):
    fig=plt.figure(figsize=(8,6))
    fig.clf()
    ax=fig.gca()
    ax.hist(img.flatten(),bins=256,cumulative=True)
    plt.show()
#im_cdf(i_mono)
