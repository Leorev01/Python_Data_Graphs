import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	#Get dates and precipitation values
	dates, precipitation = [], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			precip = float(row[3])
			
		except ValueError:
			print(f"Missing value for {current_date}")
		else:
			dates.append(current_date)
			precipitation.append(precip)

	#Plot the dates and the precipitation values
	plt.style.use('seaborn')
	fig, ax = plt.subplots()
	ax.plot(dates, precipitation, c = 'blue')

	#Format plot
	ax.set_title("Daily precipitation - 2018", fontsize = 24)
	ax.set_xlabel('Dates', fontsize = 16)
	fig.autofmt_xdate()
	ax.set_ylabel('Pricipitation recorded', fontsize = 16)
	ax.tick_params(axis = 'both', which='major', labelsize = 16)

	plt.show()