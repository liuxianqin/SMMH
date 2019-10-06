import regression
from regression import auto_prices
import matplotlib.pyplot as plt

def plot_scatter_t(auto_prices,cols,col_y='price',alpha=1.0):
	for col in cols:
		fig=plt.figure(figsize=(7,6))
		ax=fig.gca()
		auto_prices.plot.scatter(x=col,y=col_y,ax=ax,alpha=alpha)
		ax.set_title('Scanner plot of'+col_y+' vs '+col)
		ax.set_xlabel(col)
		ax.set_ylabel(col_y)
		plt.show()
num_cols=['curb_weight','engine_size','horsepower','city_mpg']
plot_scatter_t(auto_prices,num_cols,alpha=0.2)
