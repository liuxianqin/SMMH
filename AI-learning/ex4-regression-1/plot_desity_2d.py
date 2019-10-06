import regression
from regression import auto_prices
import seaborn as sns
import matplotlib.pyplot as plt
num_cols=['curb_weight','engine_size','horsepower','city_mpg']

def plot_desity_2d(auto_prices,cols,col_y='price',kind='kde'):
	for col in cols:
		sns.set_style("whitegrid")
		sns.jointplot(col,col_y,data=auto_prices,kind=kind)
		plt.xlabel(col)
		plt.ylabel(col_y)
		
	plt.show()

plot_desity_2d(auto_prices,num_cols)


plot_desity_2d(auto_prices,num_cols,kind='hex')

