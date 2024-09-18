import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/san_francisco_1996_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	for index, column_name in enumerate(header_row):
		print(index, column_name)
	
	dates, highs, lows = [], [], []
	for row in reader:
		date = datetime.strptime(row[5], '%Y-%m-%d')
		max_temp = int(row[9])
		min_temp = int(row[10])
		dates.append(date)
		highs.append(max_temp)
		lows.append(min_temp)

	plt.style.use('classic')
	fig, ax = plt.subplots()
	ax.plot(dates,highs, c = 'red', alpha = 0.5)
	ax.plot(dates, lows, c = 'blue', alpha = 0.5)
	ax.fill_between(dates, highs, lows, facecolor= 'blue',alpha = 0.1)

	ax.set_title('Daily highest and lowest temperatures in San Francisco', fontsize = 24)
	ax.set_xlabel('Dates', fontsize = 16)
	fig.autofmt_xdate()
	ax.set_ylabel('Temperature', fontsize = 16)
	ax.tick_params(axis = 'both', which = 'major', labelsize = 16)

	plt.show()