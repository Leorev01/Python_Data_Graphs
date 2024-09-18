import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

#	for index, column_name in enumerate(header_row):
#		print(index, column_name)
	dates, precipitation = [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		dates.append(current_date)
		precip = float(row[3])
		precipitation.append(precip)

	#Plot the dates and the recorded precipitation
	plt.style.use('seaborn')
	fig,ax = plt.subplots()
	ax.plot(dates, precipitation, c = 'blue')

	#Format plot

	ax.set_title('Recorded precipitation for 2018 in Death Valley', fontsize = 24)
	ax.set_xlabel('Dates', fontsize = 16)
	fig.autofmt_xdate()
	ax.set_ylabel('Precipitation Recorded', fontsize = 16)
	ax.tick_params(axis = 'both', which = 'major', labelsize = 16)

	plt.show()
