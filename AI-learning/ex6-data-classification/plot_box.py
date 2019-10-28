#coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import numpy.random as nr
import math

from ex5 import credit

def plot_box(credit,cols,col_x='bad_credit'):
	for col in cols:
		sns.set_style("whitegrid")
		sns.boxplot(col_x,col,data=credit)
		plt.xlabel(col_x)
		plt.ylabel(col)
		plt.show()

num_cols=['loan_duration_mo','loan_amount','payment_pcnt_income',
		  'age_yrs','number_loans','dependents']
plot_box(credit,num_cols)	
