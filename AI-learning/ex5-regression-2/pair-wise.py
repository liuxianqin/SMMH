#coding=utf-8

from regression import auto_prices
import seaborn as sns
import matplotlib.pyplot as plt



num_cols = ["curb_weight", "engine_size", "horsepower", "city_mpg", "price", "fuel_type"]
sns.pairplot(auto_prices[num_cols], hue='fuel_type', palette="Set2", diag_kind="kde", height=2).map_upper(sns.kdeplot, cmap="Blues_d")
plt.show()
