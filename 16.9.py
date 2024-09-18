import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/world_fires_1_day.csv'
with open (filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	num_rows = 1_000

	for index, header in enumerate(header_row):
		print(index, header)

	lat, lon, bri, hover_texts = [], [], [], []
	row_num = 0
	for row in reader:
		lat.append(row[0])
		lon.append(row[1])
		bri.append(float(row[2]))
		hover_texts.append(bri)
		row_num +=1
		if row_num == num_rows:
			break

	data = [{
		'type':'scattergeo',
		'lon':lon,
		'lat':lat,
		'text':hover_texts,
		'marker':{
			'size':[br/20 for br in bri],
			'color':bri,
			'colorscale':'Viridis',
			'reversescale':True,
			'colorbar':{'title':'Brightness'},
		}
	}]

	title = "World Fires in 1 day"

my_layout = Layout(title = title)
fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename = 'World_fires_1_day.html')