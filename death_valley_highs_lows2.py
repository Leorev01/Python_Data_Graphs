import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	for index, header in enumerate(header_row):
		print(index, header)

	dates, highs, lows, precipitation = [], [], [], []
	for row in reader:
		date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			high = int(row[4])
			low = int(row[5])
			precip = float(row[3])
		except ValueError:
			print(f"Value missing in {date}")
		else:
			dates.append(date)
			highs.append(high)
			lows.append(low)
			precipitation.append(precip*500)

	plt.style.use('classic')
	fig, ax = plt.subplots()
	ax.plot(dates,highs, c= 'red', alpha = 0.5)
	ax.plot(dates, lows, c = 'blue', alpha = 0.5)
	ax.plot(dates, precipitation, c = 'green')
	ax.fill_between(dates, highs, lows, facecolor= 'blue', alpha = 0.1)

	ax.set_title("Daily highest and lowest recorded temperatures, and (precipitation x 500)", fontsize = 24)
	ax.set_xlabel("Dates", fontsize = 16)
	fig.autofmt_xdate()
	ax.set_ylabel("Temperature, and precipitation levels x 500", fontsize = 16)
	ax.tick_params(axis= 'both', which = 'major', labelsize = 16)

	plt.show()