import regression
from regression import auto_prices
import matplotlib.pyplot as plt
def plot_bars(auto_prices,cols):
	for col in cols:
		fig=plt.figure(figsize=(6,6))
		ax=fig.gca()
		counts=auto_prices[col].value_counts()
		counts.plot.bar(ax=ax,color='blue')
		ax.set_title('Number of autos by'+col)
		ax.set_xlabel(col)
		ax.set_ylabel('Number of autos')
		plt.show()
		
plot_cols=['make','body_style','num_of_cylinders']
plot_bars(auto_prices,plot_cols)
