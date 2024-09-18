import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/significant_eq_30_day.json'
with open(filename) as f:
	all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
title = all_eq_data['metadata']['title']

mag, lon, lat, name = [], [], [], []
for dicts in all_eq_dicts:
	mag.append(dicts['properties']['mag'])
	lon.append(dicts['geometry']['coordinates'][0])
	lat.append(dicts['geometry']['coordinates'][1])
	name.append(dicts['properties']['title'])

data = [{
	'type':'scattergeo',
	'lon':lon,
	'lat':lat,
	'text':name,
	'marker':{
		'size':[5* ma for ma in mag],
		'color':mag,
		'colorscale':'Cividis',
		'reversescale':True,
		'colorbar':{'title':'Magnitude'},
	}
}]
my_layout = Layout(title = title)

fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename = 'significant_eq_30_days.html')