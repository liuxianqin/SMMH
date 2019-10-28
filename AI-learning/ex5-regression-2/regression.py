#coding=utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#%matplotlib inline

auto_prices=pd.read_csv("Automobile price data _Raw_.csv")

def clean_auto_data(auto_prices):
	cols=auto_prices.columns
	auto_prices.columns=[str.replace('-','_') for str in cols]
	cols=['price','bore','stroke','horsepower','peak_rpm']
	for column in cols:
		auto_prices.loc[auto_prices[column]=='?',column]=np.nan
	auto_prices.dropna(axis=0,inplace=True)
	
	for column in cols:
		auto_prices[column]=pd.to_numeric(auto_prices[column])
	
	return auto_prices

auto_prices=clean_auto_data(auto_prices)

print(auto_prices.columns)
print(auto_prices.head())
print(auto_prices.dtypes)
print(auto_prices.describe())









num_cols=['curb_weight','engine_size','horsepower','city_mpg']

def plot_desity_2d(auto_prices,cols,col_y='price',kind='kde'):
	for col in cols:
		sns.set_style("whitegrid")
		sns.jointplot(col,col_y,data=auto_prices,kind=kind)
		plt.xlabel(col)
		plt.ylabel(col_y)
		
	plt.show()

#plot_desity_2d(auto_prices,num_cols)
