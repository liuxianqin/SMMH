import regression
from regression import auto_prices
import matplotlib.pyplot as plt

def plot_histogram(auto_prices,cols,bins=10):
	for col in cols:
		fig=plt.figure(figsize=(6,6))
		ax=fig.gca()
		auto_prices[col].plot.hist(ax=ax,bins=bins)
		ax.set_title('Histogram of'+col)
		ax.set_xlabel(col)
		ax.set_ylabel('Number of autos')
		plt.show()
num_cols=['curb_weight','engine_size','city_mpg','price']
plot_histogram(auto_prices,num_cols)
