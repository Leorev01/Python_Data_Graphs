import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/death_valley_2018_simple.csv'
filename = 'data/sitka_weather_2018_simple.csv'
place_name = ''

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	print(header_row)
	date_index = header_row.index('DATE')
	high_index = header_row.index('TMAX')
	low_index = header_row.index('TMIN')
	name_index = header_row.index('NAME')

	#Get dates. high and low temperatures from the files
	dates, highs, lows = [], [], []
	for row in reader:
		if not place_name:
			place_name = row[name_index]
			print(place_name)

		current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
		try:
			high = int(row[high_index])
			low = int(row[low_index])
		except ValueError:
			print(f"Misisng infromation for {current_date}")
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)

#Plot the high and low temperatures
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, highs, c= 'red', alpha = 0.5)
ax.plot(dates, lows, c= 'blue', alpha = 0.5)
plt.fill_between(dates,highs,lows, facecolors = 'blue', alpha = 0.1)

#Format plot
title = f"Daily high and low temperatures - 2018\n{place_name}"
plt.title(title, fontsize = 24)
plt.xlabel('Dates', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel('Temperature', fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()