import csv
filename='sitka_weather.csv'
with open(filename) as f:
	reader=csv.reader(f)
	header_row=next(reader)
	print(header_row)
