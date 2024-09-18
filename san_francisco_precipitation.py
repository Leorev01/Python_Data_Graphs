import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/san_francisco_1996_simple.csv'
with open (filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	for index, row_number in enumerate(header_row):
		print(index, row_number)

	dates, precipitation = [], []
	for row in reader:
		current_date = datetime.strptime(row[5], '%Y-%m-%d')
		try:
			precip = float(row[6])
		except ValueError:
			print(f"Missing value for {current_date}")
		else:
			precipitation.append(precip)
			dates.append(current_date)

	plt.style.use('classic')
	fig,ax = plt.subplots()
	plt.plot(dates, precipitation, c = 'blue')

	ax.set_title('Daily precipitation in San Francisco - 1996', fontsize = 24)
	ax.set_xlabel('Dates', fontsize = 16)
	fig.autofmt_xdate()
	ax.set_ylabel('Temperature (F)', fontsize = 16)
	ax.tick_params(axis = 'both', which = 'major', labelsize = 16)

	plt.show()