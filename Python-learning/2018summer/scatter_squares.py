import matplotlib.pyplot as plt
values=list(range(1,1000))
squares=[x**2 for x in values]

plt.scatter(values,squares,c=squares,cmap=plt.cm.Blues,edgecolor='none')
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)
#plt.show()
plt.savefig('squares_plot.png',bbox_inches='tight')
