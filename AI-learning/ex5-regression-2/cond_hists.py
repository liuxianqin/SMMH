#coding=utf-8

from regression import auto_prices
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

## Function to plot conditioned histograms
def cond_hists(df, plot_cols, grid_col):
    #import matplotlib.pyplot as plt
    #import seaborn as sns
    ## Loop over the list of columns
    for col in plot_cols:          
        grid1 = sns.FacetGrid(df, col=grid_col)
        grid1.map(plt.hist, col, alpha=.7)
    return grid_col

## Define columns for making a conditioned histogram
plot_cols2 = ["length",
               "curb_weight",
               "engine_size",
               "city_mpg",
               "price"]

cond_hists(auto_prices, plot_cols2, 'drive_wheels')
plt.show()
