from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline 


die1 = Die()
die2 = Die()
results = []
for x in range(1000):
	results.append(die1.roll()+die2.roll())

frequencies = []
for i in range(1,die1.sides+die2.sides+1):
	frequencies.append(results.count(i))

x_values = list(range(1,die1.sides+die2.sides+1))
data = [Bar(x=x_values,y=frequencies)]


my_layout = Layout(
				title="Wynik tysiąca rzutów dwiema kostkami D6", 
				xaxis={'title':'Wynik'},
				yaxis={'title':'Częstość wyniku'}
			)

offline.plot({'data':data, 'layout':my_layout},filename='2xd6.html')