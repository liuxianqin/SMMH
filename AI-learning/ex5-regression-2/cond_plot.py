#coding=utf-8

from regression import auto_prices
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def cond_plot(cols):
    import IPython.html.widgets
    #import seaborn as sns
    for col in cols:
        g = sns.FacetGrid(auto_prices, col="drive_wheels", row = 'body_style', 
                      hue="fuel_type", palette="Set2", margin_titles=True)
        g.map(sns.regplot, col, "price", fit_reg = False)

num_cols = ["curb_weight", "engine_size", "city_mpg"]
cond_plot(num_cols)    
plt.show()
