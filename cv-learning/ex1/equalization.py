from test import *
import test
from skimage import exposure
from test import i_mono
from test import plt
i_eq=exposure.equalize_hist(i_mono)
imshow(i_eq,cmap='gray')
im_hist(i_eq)
im_cdf(i_eq)
