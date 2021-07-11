import csv
from plotly.graph_objs import Scattergeo,Layout
from plotly import offline

with open('data/world_fires_1_day.csv') as f:
	reader = csv.reader(f)
	header = next(reader)
	lons,lats,bright = [],[],[]
	for fire in reader:
		lats.append(fire[0])
		lons.append(fire[1])
		bright.append(float(fire[2]))

bmin = min(bright)
bmax = max(bright)
bright_norm = [(b-bmin)/(bmax-bmin)*30   for b in bright]
data = [{
	'type':'scattergeo',
	'lon':lons,
	'lat':lats,
	'marker':{
		'size':bright_norm,
		'colorbar':{'title':'Wielkość pożaru'},
		'colorscale':'Viridis',
	},
	'text':bright_norm,
	
},]


offline.plot({'data':data},filename='pozary.html')

for col in enumerate(header):
	print(col[0],col[1])

