from add_salt import i_n
from matplotlib.pyplot import imshow
def edge_sobel(image):
	from scipy import ndimage
	import skimage.color as sc
	import numpy as np
	image=sc.rgb2gray(image)
	dx=ndimage.sobel(image,1)
	dy=ndimage.sobel(image,0)
	mag=np.hypot(dx,dy)
	mag*=255.0/np.amax(mag)
	mag=mag.astype(np.uint8)
	return mag
	
i_edge=edge_sobel(i_n)
imshow(i_edge,cmap="gray")
