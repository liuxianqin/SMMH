#coding=utf-8

from regression import auto_prices
import seaborn as sns
import matplotlib.pyplot as plt

def plot_violin_hue(auto_prices, cols, col_y = 'price', hue_col = 'aspiration'):
    for col in cols:
        sns.set_style("whitegrid")
        sns.violinplot(col, col_y, data=auto_prices, hue = hue_col, split = True)
        plt.xlabel(col) # Set text for the x axis
        plt.ylabel(col_y)# Set text for y axis
        plt.show()

#plot_violin_hue(auto_prices, cat_cols)

cat_cols = ['fuel_type', 'aspiration', 'num_of_doors', 'body_style',
            'drive_wheels', 'engine_location', 'engine_type', 'num_of_cylinders'] 

plot_violin_hue(auto_prices, cat_cols)

