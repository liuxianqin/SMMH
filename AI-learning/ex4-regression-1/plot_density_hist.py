import regression
import matplotlib.pyplot as plt
from regression import auto_prices
from hist import num_cols
import seaborn as sns
def plot_density_hist(auto_prices,cols,bins=10,hist=False):
	for col in cols:
		sns.set_style("whitegrid")
		sns.distplot(auto_prices[col],bins=bins,rug=True,hist=hist)
		plt.title('Histogram of'+col)
		plt.xlabel(col)
		plt.ylabel('Number of autos')
		plt.show()
		
plot_density_hist(auto_prices,num_cols)
plot_density_hist(auto_prices,num_cols,bins=20,hist=True)
