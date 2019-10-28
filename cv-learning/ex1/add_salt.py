from equalization import i_eq
from test import *
import skimage

i_n=skimage.util.random_noise(i_eq)
plt.show(i_n)
