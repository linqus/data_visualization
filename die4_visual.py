from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline 


die1 = Die()
die2 = Die()
results = []
num_rolls = 100_000
max_rolls = die1.sides*die2.sides
for x in range(num_rolls):
	results.append(die1.roll()*die2.roll())

frequencies = []
for i in range(2,max_rolls+1):
	frequencies.append(results.count(i))

x_values = list(range(2,max_rolls+1))
data = [Bar(x=x_values,y=frequencies)]


my_layout = Layout(
				title=f"Iloczyn wyników dla {num_rolls} rzutów dwiema kostkami D6", 
				xaxis={'title':'Wynik','dtick':1},
				yaxis={'title':'Częstość wyniku'}
			)

offline.plot({'data':data, 'layout':my_layout},filename='d6_x_d6.html')