from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline 


die = Die()
results = []
for x in range(1000):
	results.append(die.roll())

frequencies = []
for i in range(1,die.sides+1):
	frequencies.append(results.count(i))

x_values = list(range(1,die.sides+1))
data = [Bar(x=x_values,y=frequencies)]


my_layout = Layout(
				title="Wynik tysiąca rzutów kostką D6", 
				xaxis={'title':'Wynik'},
				yaxis={'title':'Częstość wyniku'}
			)

offline.plot({'data':data, 'layout':my_layout},filename='d6.html')