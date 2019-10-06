import matplotlib.pyplot as plt
from random_walk import RandomWalk
rw=RandomWalk()
rw.fill_walk() 
point_numbers=list(range(rw.num_points))

plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,s=1)
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()
	
	
	
