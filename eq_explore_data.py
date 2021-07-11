import json
from plotly import offline
from plotly.graph_objs import Scattergeo, Layout

filename = 'data/eq_data_30_day_m1.json'
with open(filename) as file:
	all_eq_data = json.load(file)

# print(len(all_eq_data['features']))

lons, lats, mags, texts = [],[],[],[]

for eq in all_eq_data['features']:
	mags.append(eq['properties']['mag'])
	lons.append(eq['geometry']['coordinates'][0])
	lats.append(eq['geometry']['coordinates'][1])
	texts.append(eq['properties']['title'])

layout = Layout(title=all_eq_data['metadata']['title'])
data = [{
			'type':'scattergeo',
			'lon':lons,
			'lat':lats,
			'marker':{
				'size':[mag*5 for mag in mags ],
				'color':mags,
				'colorscale':'Viridis',
				'reversescale':True,
				'colorbar':{'title':'Magnitude'}
			},
			'text':texts

		},]


offline.plot({'data':data,'layout':layout},filename='eq.html')