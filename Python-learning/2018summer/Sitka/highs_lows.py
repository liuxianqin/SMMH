import csv
from datetime import datetime
from matplotlib import pyplot as plt
filename='sitka_weather_2014.csv'
with open(filename) as f:
	reader=csv.reader(f)
	header_row=next(reader)
	dates,highs,lows=[],[],[]
	for row in reader:
		high=int(row[1])
		highs.append(high)
		low=int(row[3])
		lows.append(low)
		current_date=datetime.strptime(row[0],"%Y-%m-%d")
		dates.append(current_date)
	print(highs)
for index,column_header in enumerate(header_row):
	print(index,column_header)

fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
plt.title("Daily high temperatures,July 2014",fontsize=24)
fig.autofmt_xdate()
plt.xlabel('',fontsize=16)
plt.ylabel("Temperature",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()
