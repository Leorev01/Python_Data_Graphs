import csv
import matplotlib.pyplot as plt
from datetime import datetime

def get_weather_data(filename, dates, highs, lows,date_index, high_index, low_index):
	"""Get highs and lows from the data file"""
	with open (filename) as f:
		reader = csv.reader(f)
		header_row = next(reader)

		for row in reader:
			current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
			try:
				high = int(row[high_index])
				low = int(row[low_index])
			except ValueError:
				print(f"Missing value for {current_date}")
			else:
				dates.append(current_date)
				highs.append(high)
				lows.append(low)

#Get weather data for death valley
filename = 'data/death_valley_2018_simple.csv'
dates, highs, lows = [], [], []
get_weather_data(filename, dates, highs, lows, date_index=2, high_index=6, low_index=5)

fig,ax = plt.subplots()
plt.style.use('classic')
ax.plot(dates, highs, c = 'red', alpha = 0.5)
ax.plot(dates, lows, c = 'blue', alpha = 0.5)
ax.fill_between(dates, highs, lows, facecolors = 'blue', alpha = 0.1)

#Get weather dta for San Francisco
filename = 'data/sitka_weather_2018_simple.csv'
dates, highs, lows = [], [], []
get_weather_data(filename, dates, highs, lows, date_index = 2, high_index = 5, low_index = 6)
plt.plot(dates, highs, c= 'orange', alpha = 0.5)
plt.plot(dates, lows, c= 'green', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolors = 'green', alpha = 0.1)

title = 'Daily high and low temperature values'
title += 'in Death Valley and San Francisco'
plt.title(title, fontsize = 24)
plt.xlabel('Dates', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel('Temeperature', fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()