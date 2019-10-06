import regression
from regression import auto_prices
#from regression import num_cols
import matplotlib.pyplot as plt


def plot_scatter(auto_prices,cols,col_y='price'):
	for col in cols:
		fig=plt.figure(figsize=(7,6))
		ax=fig.gca()
		auto_prices.plot.scatter(x=col,y=col_y,ax=ax)
		ax.set_title('Scatter plot of'+col_y+' vs '+col)
		ax.set_xlabel(col)
		ax.set_ylabel(col_y)
		plt.show()


num_cols=['curb_weight','engine_size','horsepower','city_mpg']
plot_scatter(auto_prices,num_cols)

plot_scatter(auto_prices,['horsepower'],'engine_size')
